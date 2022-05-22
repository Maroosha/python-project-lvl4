from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.translation import gettext_lazy
from .models import Task

User = get_user_model()


class TasksTests(TestCase):
    "Test tasks."
    fixtures = [
        'users.json',
        'statuses.json',
        'tasks.json',
        'tasklabelrelation.json',
        'labels.json',
    ]
    def setUp(self):
        "Set up statuses."
        # Tasks are seen by logged in users only => self.user
        self.user1 = User.objects.get(pk=1)
        self.user2 = User.objects.get(pk=2)
        self.user3 = User.objects.get(pk=3)

        self.task1 = Task.objects.get(pk=1)
        self.task2 = Task.objects.get(pk=2)
        self.task3 = Task.objects.get(pk=4)



    def test_tasks_list(self):
        "Test list of tasks page."
        self.client.force_login(self.user1)
        response = self.client.get(reverse('tasks:list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            template_name='tasks.html',
        )

        tasks_list = list(response.context['tasks'])
        self.assertQuerysetEqual(
            tasks_list,
            [self.task1, self.task2, self.task3],
        )


    def test_create_task(self):
        "Test create a task."
        self.client.force_login(self.user1)
        response = self.client.get(reverse('tasks:create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            template_name='form.html',
        )

        new_task = {
            'name': 'new task',
            'description': 'bla bla',
            'status': 2,
            'created_by': 1,
            'executive': 3,
        }
        response = self.client.post(
            reverse('tasks:create'),
            new_task,
            follow=True,
        )

        self.assertRedirects(response, '/tasks/', status_code=302)
        self.assertContains(
            response,
            gettext_lazy('Task successfully created.'),
        )

        task = Task.objects.get(name=new_task['name'])
        self.assertEqual('bla bla', task.description)
        self.assertEqual(5, task.id)


    def test_update_task(self):
        "Test update task."
        self.client.force_login(self.user1)
        task = self.task3
        response = self.client.get(reverse('tasks:change', args=(task.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            template_name='form.html',
        )

        changed_task = {
            'name': 'updated task',
            'description': 'bla bla bla',
            'status': 1,
            'created_by': 1,
            'executive': 1,
        }
        response = self.client.post(
            reverse('tasks:change', args=(task.id,)),
            changed_task,
            follow=True,
        )

        self.assertRedirects(response, '/tasks/', status_code=302)
        self.assertContains(
            response,
            gettext_lazy('Task successfully changed.'),
        )
        new_task = Task.objects.get(name=changed_task['name'])
        self.assertEqual(task.id, new_task.id)


    def test_delete_task(self):
        "Test delete task."
        self.client.force_login(self.user2)
        task = self.task2
        response = self.client.get(reverse('tasks:delete', args=(task.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            template_name='delete.html',
        )

        response = self.client.post(
            reverse('tasks:delete', args=(task.id,)),
            follow=True,
        )

        with self.assertRaises(Task.DoesNotExist):
            Task.objects.get(pk=task.id)
        self.assertRedirects(response, '/tasks/', status_code=302)
        self.assertContains(response, gettext_lazy('Task successfully deleted.'))


    def test_delete_task_by_non_creator(self):
        "Delete task by a non-creator."
        self.client.force_login(self.user3)
        task = self.task3
        response = self.client.get(reverse('tasks:delete', args=(task.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            template_name='delete.html',
        )

        response = self.client.post(
            reverse('tasks:delete', args=(task.id,)),
            follow=True,
        )
        self.assertTrue(Task.objects.filter(pk=task.id).exists())
        self.assertRedirects(response, '/tasks/')
        self.assertContains(
            response,
            gettext_lazy('The task can only be deleted by its creator.'),
        )


    def test_filter_by_status(self):
        "Filter the tasks by status."
        self.client.force_login(self.user1)
        filtered_by_status = f'{reverse("tasks:list")}?status=2'
        response = self.client.get(filtered_by_status)
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(list(response.context['tasks']), [self.task3])


    def test_filter_by_executive(self):
        "Filter the tasks by executive."
        self.client.force_login(self.user1)
        filtered_by_executive = f'{reverse("tasks:list")}?executive=2'
        response = self.client.get(filtered_by_executive)
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(list(response.context['tasks']), [self.task1])


    def test_filter_by_label(self):
        "Filter the tasks by label."
        self.client.force_login(self.user1)
        filtered_by_label = f'{reverse("tasks:list")}?label=1'
        response = self.client.get(filtered_by_label)
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(list(response.context['tasks']), [self.task1])


    def test_filter_by_own_tasks(self):
        "Filter by own tasks."
        self.client.force_login(self.user2)
        filtered_by_own_tasks = f'{reverse("tasks:list")}?own_task=on'
        response = self.client.get(filtered_by_own_tasks)
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(list(response.context['tasks']), [self.task1, self.task2])
