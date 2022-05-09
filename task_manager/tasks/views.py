from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy
from django.contrib.auth import get_user_model
from .models import Task
from .forms import TaskForm

User = get_user_model()


class TaskList(LoginRequiredMixin, ListView):
    "Show the list of tasks."
    model = Task
    template_name = 'tasks.html'
    context_object_name = 'tasks'


    def get_context_data(self, **kwargs):
        "Define the title."
        context = super().get_context_data(**kwargs)
        context['title'] = gettext_lazy('Tasks')
        return context


class CreateTask(
    LoginRequiredMixin,
    SuccessMessageMixin,
    CreateView,
):
    "Create a new task."
    model = Task
    template_name = 'form.html'
    form_class = TaskForm
    success_url = reverse_lazy('tasks:list')
    success_message = gettext_lazy('Task successfully created.')


# https://stackoverflow.com/questions/55092544/django-and-the-form-valid-method
# https://github.com/django/django/search?p=1&q=form_valid
    def form_valid(self, form):
        """
        Add the user as a task auther.

        Called when correct data is entered into the form
        and the form has been successfully validated without any errors.
        """
        form.instance.created_by = User.objects.get(pk=self.request.user.pk)
        return super().form_valid(form)


    def get_context_data(self, **kwargs):
        "Define the title and the button."
        context = super().get_context_data(**kwargs)
        context['title'] = gettext_lazy('Create a task')
        context['button_text'] = gettext_lazy('Create')
        return context


class ChangeTask(
    LoginRequiredMixin,
    SuccessMessageMixin,
    UpdateView,
):
    "Change a task."
    model = Task
    template_name = 'form.html'
    form_class = TaskForm
    success_url = reverse_lazy('tasks:list')
    success_message = gettext_lazy('Task successfully changed.')


    def get_context_data(self, **kwargs):
        "Define title and button."
        context = super().get_context_data(**kwargs)
        context['title'] = gettext_lazy('Change a task')
        context['button_text'] = gettext_lazy('Change')
        return context


class DeleteTask(
    LoginRequiredMixin,
    SuccessMessageMixin,
    DeleteView,
):
    "Delete a task."
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('tasks:list')
    success_message = gettext_lazy('Task successfully deleted.')


# https://stackoverflow.com/questions/55092544/django-and-the-form-valid-method
    def form_valid(self, form):
        "Check if the user is an author of a task."
        error_message = gettext_lazy('The task can only be deleted by its creator.')
        if self.get_object().created_by != self.request.user:
            messages.error(self.request, error_message)
        else:
            super().form_valid(form)
        return redirect(self.success_url)


    def get_context_data(self, **kwargs):
        "Define the title and the button."
        context = super().get_context_data(**kwargs)
        context['title'] = gettext_lazy('Delete a task')
        context['button_text'] = gettext_lazy('Delete')
        return context
