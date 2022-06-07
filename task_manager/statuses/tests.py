from django.test import TestCase
from django.urls import reverse
from faker import Faker
from task_manager.tasks.models import Task
from task_manager.users.models import User
from .models import Status
from .constants import (
    DELETE_TEMPLATE,
    ERROR_STATUS_IN_USE,
    FORM_TEMPLATE,
    NAME,
    STATUS_CHANGED,
    STATUS_CREATED,
    STATUS_DELETED,
    STATUS_LIST_TEMPLATE,
)


class StatusesTest(TestCase):
    "Test Statuses app."
    fixtures = [
        'users.json',
        'statuses.json',
        'tasks.json',
    ]

    def setUp(self):
        "Set up statuses."
        self.faker = Faker()
        # Statuses are seen by logged in users only => self.user
        self.user = User.objects.get(pk=2)
        self.status1 = Status.objects.get(pk=1)
        self.status2 = Status.objects.get(pk=2)
        self.task1 = Task.objects.get(pk=1)
        self.task2 = Task.objects.get(pk=2)

    def test_statuses_list(self):
        "Test list of statuses."
        self.client.force_login(self.user)
        response = self.client.get(reverse('statuses:list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            template_name=STATUS_LIST_TEMPLATE
        )

        statuses_list = list(response.context['statuses'])
        status1, status2 = statuses_list
        self.assertEqual(status1.name, 'Jane Doe\'s status')
        self.assertEqual(status1.id, 1)
        self.assertEqual(status2.name, 'John Smith\'s status')
        self.assertEqual(status2.id, 2)

    def test_create_status(self):
        "Test create status."
        self.client.force_login(self.user)
        response = self.client.get(reverse('statuses:create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            template_name=FORM_TEMPLATE,
        )

        Faker.seed(1)
        name = self.faker.word()
        new_status = {
            NAME: name,
        }
        response = self.client.post(
            reverse('statuses:create'),
            new_status,
            follow=True,
        )

        self.assertRedirects(response, '/statuses/', status_code=302)
        self.assertContains(
            response,
            STATUS_CREATED,
        )

        status = Status.objects.get(name=new_status['name'])
        self.assertEqual(3, status.id)

    def test_change_status(self):
        "Test change status."
        self.client.force_login(self.user)
        status = self.status1
        response = self.client.get(
            reverse('statuses:change', args=(status.id,)),
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            template_name=FORM_TEMPLATE,
        )

        Faker.seed(2)
        name = self.faker.word()
        changed_status = {
            NAME: name,
        }
        response = self.client.post(
            reverse('statuses:change', args=(status.id,)),
            changed_status,
            follow=True,
        )

        self.assertRedirects(response, '/statuses/', status_code=302)
        self.assertContains(
            response,
            STATUS_CHANGED,
        )
        new_status = Status.objects.get(name=changed_status['name'])
        self.assertEqual(status.id, new_status.id)

    def test_delete_status_with_tasks(self):
        "Test delete status with tasks."
        self.client.force_login(self.user)
        status = self.status1
        response = self.client.post(
            reverse('statuses:delete', args=(status.id,)),
            follow=True,
        )
        self.assertTrue(User.objects.filter(pk=status.id).exists())
        self.assertRedirects(response, '/statuses/')
        self.assertContains(response, ERROR_STATUS_IN_USE)

    def test_delete_status(self):
        "Test delete status."
        self.client.force_login(self.user)
        status = self.status1
        self.task1.delete()
        self.task2.delete()
        response = self.client.get(
            reverse('statuses:delete', args=(status.id,)),
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            template_name=DELETE_TEMPLATE,
        )

        response = self.client.post(
            reverse('statuses:delete', args=(status.id,)),
            follow=True,
        )

        with self.assertRaises(Status.DoesNotExist):
            Status.objects.get(pk=status.id)
        # Redirects and messages
        self.assertRedirects(response, '/statuses/', status_code=302)
        self.assertContains(response, STATUS_DELETED)
