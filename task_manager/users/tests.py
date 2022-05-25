from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from task_manager.tasks.models import Task
from task_manager.statuses.models import Status
from .constants import (
    DELETE_TEMPLATE,
    ERROR_USER_IN_USE,
    FIRST_NAME,
    FORM_TEMPLATE,
    LAST_NAME,
    PASSWORD1,
    PASSWORD2,
    STATUSES_FIXTURE,
    TASKS_FIXTURE,
    USER_CHANGED,
    USER_CREATED,
    USER_DELETED,
    USER_LIST_TEMPLATE,
    USERNAME,
    USERS_FIXTURE,
)

User = get_user_model()


class UsersTest(TestCase):
    "Test Users app."
    fixtures = [USERS_FIXTURE, STATUSES_FIXTURE, TASKS_FIXTURE]

    def setUp(self):
        "Set up users."
        self.user1 = User.objects.get(pk=1)
        self.user2 = User.objects.get(pk=2)
        self.user3 = User.objects.get(pk=3)
        self.status1 = Status.objects.get(pk=1)
        self.status2 = Status.objects.get(pk=2)
        self.task1 = Task.objects.get(pk=1)
        self.task2 = Task.objects.get(pk=2)
        self.task3 = Task.objects.get(pk=4)


    def test_users_list(self):
        "Test users list."
        # Issue a GET request.
        response = self.client.get(reverse('users:list'))
        self.assertTemplateUsed(
            response,
            template_name=USER_LIST_TEMPLATE,
        )
        users_list = list(response.context['users'])
        user1, user2, user3 = users_list
        # Checking whether the response is 200 OK.
        self.assertEqual(response.status_code, 200)
        # Checking whether the user info is correct
        self.assertEqual(user1.username, 'jsmith')
        self.assertEqual(user1.first_name, 'John')
        self.assertEqual(user1.last_name, 'Smith')
        self.assertEqual(user2.username, 'janedoe')
        self.assertEqual(user2.first_name, 'Jane')
        self.assertEqual(user2.last_name, 'Doe')
        self.assertEqual(user3.username, 'qwerty')
        self.assertEqual(user3.first_name, 'qwerty')
        self.assertEqual(user3.last_name, 'qwerty')


    def test_create_user(self):
        "Test create user."
        # Check response
        response = self.client.get(reverse('users:create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(  # check the template used
            response,
            template_name=FORM_TEMPLATE,
        )

        # Create a new user
        new_user = {
            FIRST_NAME: 'Thorin',
            LAST_NAME: 'Oakenshield',
            USERNAME: 'th.oakenshield',
            PASSWORD1: 'qwerty',
            PASSWORD2: 'qwerty',
        }
        response = self.client.post(
            reverse('users:create'),
            new_user,
            follow=True,  # the client follows any redirects
        )

        # redirect to Login, check response status
        self.assertRedirects(response, '/login/', status_code=302)
        self.assertContains(
            response,
            USER_CREATED,
        )
        # Check user details
        new_user = User.objects.get(username=new_user['username'])
        self.assertEqual('Thorin', new_user.first_name)
        self.assertEqual('Oakenshield', new_user.last_name)
        self.assertTrue(new_user.check_password('qwerty'))


    def test_change_user(self):
        "Test change user."
        # Gonna change the user with pk=1 (self.user1)
        user = self.user1
        # use the force_login() method to simulate the effect
        # of a user logging into the site
        self.client.force_login(User.objects.get(pk=user.id))
        response = self.client.get(reverse('users:change', args=(user.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            template_name=FORM_TEMPLATE,
        )

        # introducing changes
        changed_user = {
            FIRST_NAME: 'Mr.',
            LAST_NAME: 'Underhill',
            USERNAME: 'funderhill',
            PASSWORD1: 'q1w2e3r4',
            PASSWORD2: 'q1w2e3r4',
        }
        response = self.client.post(
            reverse('users:change', args=(user.id,)),
            changed_user,
            follow=True,
        )

        # redirect to Users, check response status
        self.assertRedirects(response, '/users/', status_code=302)
        self.assertContains(
            response,
            USER_CHANGED,
        )
        # Check user details
        new_user = User.objects.get(username=changed_user['username'])
        self.assertEqual('Mr.', new_user.first_name)
        self.assertEqual('Underhill', new_user.last_name)
        self.assertTrue(new_user.check_password('q1w2e3r4'))


    def test_delete_user_with_tasks(self):
        "Test delete user with a task."
        user = self.user2  # creator of task2
        self.client.force_login(user)
#        self.client.force_login(User.objects.get(pk=user.id))
        response = self.client.post(
            reverse('users:delete', args=(user.id,)),
            follow=True,
        )
        self.assertTrue(User.objects.filter(pk=user.id).exists())
        self.assertRedirects(response, '/users/')
        self.assertContains(
            response,
            ERROR_USER_IN_USE,
        )


    def test_delete_user(self):
        "Test delete user."
        Task.objects.all().delete()
        Status.objects.all().delete()
        user = self.user1
        self.client.force_login(user)
        response = self.client.get(reverse('users:delete', args=(user.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            template_name=DELETE_TEMPLATE,
        )

        # deleting a user (user1)
        response = self.client.post(
            reverse('users:delete', args=(user.id,)),
            follow=True,
        )

        # make sure the user does not exist anymore
        with self.assertRaises(User.DoesNotExist):
            User.objects.get(pk=user.id)
        # Redirects and messages
        self.assertRedirects(response, '/users/', status_code=302)
        self.assertContains(response, USER_DELETED)
