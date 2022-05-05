from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.translation import gettext_lazy
from faker import Faker
from .models import Status

User = get_user_model()


class StatusesTest(TestCase):
    "Test Users app."
    fixtures = ['statuses.json', 'users.json']

    def setUp(self):
        "Set up statuses."
        self.faker = Faker()
        # Statuses are seen by logged in users only => self.user
        self.user = User.objects.get(pk=3)
        self.status1 = Status.objects.get(pk=1)
        self.status2 = Status.objects.get(pk=2)


    def test_statuses_list(self):
        "Test list of statuses."
        self.client.force_login(self.user)
        response = self.client.get(reverse('statuses:list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            template_name='statuses.html',
        )

        statuses_list = list(response.context['statuses'])
        status1, status2 = statuses_list
        self.assertEqual(status1.name, 'new_status')
        self.assertEqual(status1.id, 1)
        self.assertEqual(status2.name, 'nnss')
        self.assertEqual(status2.id, 2)


    def test_create_status(self):
        "Test create status."
        self.client.force_login(self.user)
        response = self.client.get(reverse('statuses:create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            template_name='form.html',
        )

        Faker.seed(1)
        name = self.faker.word()
        new_status = {
            'name': name,
        }
        response = self.client.post(
            reverse('statuses:create'),
            new_status,
            follow=True,
        )

        self.assertRedirects(response, '/statuses/', status_code=302)
        self.assertContains(
            response,
            gettext_lazy('Status successfully created.'),
        )

        status = Status.objects.get(name=new_status['name'])
        self.assertEqual(3, status.id)


    def test_change_status(self):
        "Test change status."
        self.client.force_login(self.user)
        status = self.status1
        response = self.client.get(reverse('statuses:change', args=(status.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            template_name='form.html',
        )

        Faker.seed(2)
        name = self.faker.word()
        changed_status = {
            'name': name,
        }
        response = self.client.post(
            reverse('statuses:change', args=(status.id,)),
            changed_status,
            follow=True,
        )

        self.assertRedirects(response, '/statuses/', status_code=302)
        self.assertContains(
            response,
            gettext_lazy('Status successfully changed.'),
        )
        new_status = Status.objects.get(name=changed_status['name'])
        self.assertEqual(status.id, new_status.id)


    def test_delete_status(self):
        "Test delete status."
        self.client.force_login(self.user)
        status = self.status1
        response = self.client.get(reverse('statuses:delete', args=(status.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            template_name='delete.html',
        )

        response = self.client.post(
            reverse('statuses:delete', args=(status.id,)),
            follow=True,
        )

        with self.assertRaises(Status.DoesNotExist):
            Status.objects.get(pk=status.id)
        # Redirects and messages
        self.assertRedirects(response, '/statuses/', status_code=302)
        self.assertContains(response, gettext_lazy('Status successfully deleted.'))
