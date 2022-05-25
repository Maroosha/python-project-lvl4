from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import ProtectedError
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.urls import reverse_lazy
from .forms import CreateUserForm
from django.contrib.auth import get_user_model
from .constants import (
    BUTTON_NAME_TITLE,
    BUTTON_TEXT,
    CHANGE_BUTTON,
    CHANGE_USER_TITLE,
    CREATE_USER_TITLE,
    DELETE_BUTTON,
    DELETE_TEMPLATE,
    DELETE_USER_TITLE,
    ERROR_USER_IN_USE,
    FORM_TEMPLATE,
    REGISTER_BUTTON,
    USER_CHANGED,
    USER_CREATED,
    USER_DELETED,
    USER_LIST_TEMPLATE,
    USER_LIST_TITLE,
)
from .custom_mixins import (
    EditUserCustomMixin,
    LoginRequiredCustomMixin,
)

User = get_user_model()


class UserList(ListView):
    "Show the list of users."
    template_name = USER_LIST_TEMPLATE
    model = User
    context_object_name = 'users'

    def get_context_data(self, **kwargs):
        '.'
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
        "Set up the title ad the button."
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
    SuccessMessageMixin,
    EditUserCustomMixin,
    DeleteView,
):
    "Delete a user."
    model = User
    template_name = DELETE_TEMPLATE
    success_url = reverse_lazy('users:list')
    success_message = USER_DELETED
    error_message = ERROR_USER_IN_USE

    def get_context_data(self, **kwargs):
        "Set up the title ad the button."
        context = super().get_context_data(**kwargs)
        context[BUTTON_NAME_TITLE] = DELETE_USER_TITLE
        context[BUTTON_TEXT] = DELETE_BUTTON
        return context

    def form_valid(self, form):
        "Check if any statuses or tasks are assigned to the given user."
        try:
            self.object.delete()
        except ProtectedError:
            messages.error(self.request, self.error_message)
        else:
            messages.success(self.request, self.success_message)
        return HttpResponseRedirect(self.success_url)
