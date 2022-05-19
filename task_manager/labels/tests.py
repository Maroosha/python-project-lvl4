from cProfile import label
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.translation import gettext_lazy
from task_manager.statuses.models import Status
from task_manager.tasks.models import Task
from .models import Label

User = get_user_model()


class LabelsTests(TestCase):
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
        self.user1 = User.objects.get(pk=1)
        self.user2 = User.objects.get(pk=2)
        self.user3 = User.objects.get(pk=3)

        self.status1 = Status.objects.get(pk=1)
        self.status2 = Status.objects.get(pk=2)

        self.task1 = Task.objects.get(pk=1)
        self.task2 = Task.objects.get(pk=2)
        self.task3 = Task.objects.get(pk=4)

        self.label1 = Label.objects.get(pk=1)
        self.label2 = Label.objects.get(pk=2)
        self.label3 = Label.objects.get(pk=3)
        self.label4 = Label.objects.get(pk=4)


    def test_labels_list(self):
        "Test list of labels page."
        self.client.force_login(self.user2)
        response = self.client.get(reverse('labels:list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            template_name='labels.html',
        )

        tasks_list = list(response.context['labels'])
        self.assertQuerysetEqual(
            tasks_list,
            [self.label1, self.label2, self.label3, self.label4],
        )


    def test_create_label(self):
        "Test create a labels."
        self.client.force_login(self.user1)
        response = self.client.get(reverse('labels:create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            template_name='form.html',
        )

        new_label = {
            'name': 'new label',
        }
        response = self.client.post(
            reverse('labels:create'),
            new_label,
            follow=True,
        )

        self.assertRedirects(response, '/labels/', status_code=302)
        self.assertContains(
            response,
            gettext_lazy('Label successfully created.'),
        )

        lbl = Label.objects.get(name=new_label['name'])
        self.assertEqual(5, lbl.id)


    def test_update_label(self):
        "Test update a label."
        self.client.force_login(self.user3)
        label_ = self.label3
        response = self.client.get(reverse('labels:change', args=(label_.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            template_name='form.html',
        )

        changed_label = {
            'name': 'changed lbl',
        }
        response = self.client.post(
            reverse('labels:change', args=(label_.id,)),
            changed_label,
            follow=True,
        )

        self.assertRedirects(response, '/labels/', status_code=302)
        self.assertContains(
            response,
            gettext_lazy('Label successfully changed.'),
        )
        new_label = Label.objects.get(name=changed_label['name'])
        self.assertEqual(label_.id, new_label.id)


    def test_delete_label_with_task(self):  # WON'T WORK
        "Test deleting a label with a task assigned to it."
        self.client.force_login(self.user2)
        label_ = self.label4
        response = self.client.post(
            reverse('labels:delete', args=(label_.pk,)),
            follow=True,
        )
        self.assertTrue(Label.objects.filter(pk=label_.pk).exists())
        self.assertRedirects(response, '/labels/')
        self.assertContains(
            response,
            gettext_lazy('Cannot delete a label in use.'),
        )


    def test_delete_label(self):
        "Test delete a label."
        self.client.force_login(self.user2)
        Task.objects.all().delete()
        Status.objects.all().delete()
        label_ = self.label2
        response = self.client.get(reverse('labels:delete', args=(label_.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            template_name='delete.html',
        )

        response = self.client.post(
            reverse('labels:delete', args=(label_.id,)),
            follow=True,
        )

        with self.assertRaises(Label.DoesNotExist):
            Label.objects.get(pk=label_.id)
        self.assertRedirects(response, '/labels/', status_code=302)
        self.assertContains(response, gettext_lazy('Label successfully deleted.'))
