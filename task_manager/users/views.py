from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.urls import reverse_lazy
from task_manager.custom_mixins import FormValidMixin
from .forms import CreateUserForm
from .models import User
from .constants import (
    BUTTON_NAME_TITLE,
    BUTTON_TEXT,
    CHANGE_BUTTON,
    CHANGE_USER_TITLE,
    CREATE_USER_TITLE,
    DELETE_BUTTON,
    DELETE_TEMPLATE,
    DELETE_USER_TITLE,
    FORM_TEMPLATE,
    REGISTER_BUTTON,
    USER_CHANGED,
    USER_CREATED,
    USER_LIST_TEMPLATE,
    USER_LIST_TITLE,
)
from .custom_mixins import (
    EditUserCustomMixin,
    LoginRequiredCustomMixin,
)


class UserList(ListView):
    "Show the list of users."
    template_name = USER_LIST_TEMPLATE
    model = User
    context_object_name = 'users'

    def get_context_data(self, **kwargs):
        'Set up the button.'
        context = super().get_context_data(**kwargs)
        context[BUTTON_NAME_TITLE] = USER_LIST_TITLE
        return context


class CreateUser(SuccessMessageMixin, CreateView):
    "Create a user."
    model = User
    template_name = FORM_TEMPLATE
    form_class = CreateUserForm
    success_url = reverse_lazy('login')
    success_message = USER_CREATED

    def get_context_data(self, **kwargs):
        "Set up the title and the button."
        context = super().get_context_data(**kwargs)
        context[BUTTON_NAME_TITLE] = CREATE_USER_TITLE
        context[BUTTON_TEXT] = REGISTER_BUTTON
        return context


class ChangeUser(
    LoginRequiredCustomMixin,
    EditUserCustomMixin,
    SuccessMessageMixin,
    UpdateView,
):
    "Change a user."
    model = User
    template_name = FORM_TEMPLATE
    form_class = CreateUserForm
    success_url = reverse_lazy('users:list')
    success_message = USER_CHANGED

    def get_context_data(self, **kwargs):
        "Set up the title ad the button."
        context = super().get_context_data(**kwargs)
        context[BUTTON_NAME_TITLE] = CHANGE_USER_TITLE
        context[BUTTON_TEXT] = CHANGE_BUTTON
        return context


class DeleteUser(
    LoginRequiredCustomMixin,
    EditUserCustomMixin,
    FormValidMixin,
    DeleteView,
):
    "Delete a user."
    model = User
    template_name = DELETE_TEMPLATE
    success_url = reverse_lazy('users:list')

    def get_context_data(self, **kwargs):
        "Set up the title ad the button."
        context = super().get_context_data(**kwargs)
        context[BUTTON_NAME_TITLE] = DELETE_USER_TITLE
        context[BUTTON_TEXT] = DELETE_BUTTON
        return context
