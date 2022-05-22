from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.views.generic import CreateView, DeleteView, UpdateView
from django_filters.views import FilterView
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy
from django.contrib.auth import get_user_model
from .models import Task
from .filters import FilterTasks
from .forms import TaskForm
from .constants import (
    BUTTON_NAME_TITLE,
    BUTTON_TEXT,
    CHANGE_BUTTON,
    CREATE_BUTTON,
    CHANGE_TASK_TITLE,
    CREATE_TASK_TITLE,
    DELETE_BUTTON,
    DELETE_TEMPLATE,
    DELETE_TASK_TITLE,
    ERROR_DELETE_TASK_BY_NONCREATOR,
    FORM_TEMPLATE,
    SHOW_BUTTON,
    TASK_CHANGED,
    TASK_CREATED,
    TASK_DELETED,
    TASK_LIST_TEMPLATE,
    TASK_LIST_TITLE,
)

User = get_user_model()


class TaskList(LoginRequiredMixin, FilterView):
    "Show the list of tasks."
    model = Task
    template_name = TASK_LIST_TEMPLATE
    context_object_name = 'tasks'
    filterset_class = FilterTasks


    def get_context_data(self, **kwargs):
        "Define the title and button text."
        context = super().get_context_data(**kwargs)
        context[BUTTON_NAME_TITLE] = gettext_lazy(TASK_LIST_TITLE)
        context[BUTTON_TEXT] = gettext_lazy(SHOW_BUTTON)
        return context


class CreateTask(
    LoginRequiredMixin,
    SuccessMessageMixin,
    CreateView,
):
    "Create a new task."
    model = Task
    template_name = FORM_TEMPLATE
    form_class = TaskForm
    success_url = reverse_lazy('tasks:list')
    success_message = gettext_lazy(TASK_CREATED)


# https://stackoverflow.com/questions/55092544/django-and-the-form-valid-method
# https://github.com/django/django/search?p=1&q=form_valid
    def form_valid(self, form):
        """
        Add the user as a task creator.

        Called when correct data is entered into the form
        and the form has been successfully validated without any errors.
        """
        form.instance.created_by = User.objects.get(pk=self.request.user.pk)
        return super().form_valid(form)


    def get_context_data(self, **kwargs):
        "Define the title and the button."
        context = super().get_context_data(**kwargs)
        context[BUTTON_NAME_TITLE] = gettext_lazy(CREATE_TASK_TITLE)
        context[BUTTON_TEXT] = gettext_lazy(CREATE_BUTTON)
        return context


class ChangeTask(
    LoginRequiredMixin,
    SuccessMessageMixin,
    UpdateView,
):
    "Change a task."
    model = Task
    template_name = FORM_TEMPLATE
    form_class = TaskForm
    success_url = reverse_lazy('tasks:list')
    success_message = gettext_lazy(TASK_CHANGED)


    def get_context_data(self, **kwargs):
        "Define title and button."
        context = super().get_context_data(**kwargs)
        context[BUTTON_NAME_TITLE] = gettext_lazy(CHANGE_TASK_TITLE)
        context[BUTTON_TEXT] = gettext_lazy(CHANGE_BUTTON)
        return context


class DeleteTask(
    LoginRequiredMixin,
    SuccessMessageMixin,
    DeleteView,
):
    "Delete a task."
    model = Task
    template_name = DELETE_TEMPLATE
    success_url = reverse_lazy('tasks:list')
    success_message = gettext_lazy(TASK_DELETED)


# https://stackoverflow.com/questions/55092544/django-and-the-form-valid-method
    def form_valid(self, form):
        "Check if the user is an author of a task."
        error_message = gettext_lazy(ERROR_DELETE_TASK_BY_NONCREATOR)
        if self.get_object().created_by != self.request.user:
            messages.error(self.request, error_message)
        else:
            super().form_valid(form)
        return redirect(self.success_url)


    def get_context_data(self, **kwargs):
        "Define the title and the button."
        context = super().get_context_data(**kwargs)
        context[BUTTON_NAME_TITLE] = gettext_lazy(DELETE_TASK_TITLE)
        context[BUTTON_TEXT] = gettext_lazy(DELETE_BUTTON)
        return context
