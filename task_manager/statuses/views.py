from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.urls import reverse_lazy

from task_manager.custom_mixins import FormValidMixin
from .models import Status
from .forms import StatusForm
from .constants import (
    BUTTON_NAME_TITLE,
    BUTTON_TEXT,
    CHANGE_BUTTON,
    CREATE_BUTTON,
    CHANGE_STATUS_TITLE,
    CREATE_STATUS_TITLE,
    DELETE_BUTTON,
    DELETE_TEMPLATE,
    DELETE_STATUS_TITLE,
    FORM_TEMPLATE,
    STATUS_CHANGED,
    STATUS_CREATED,
    STATUS_LIST_TEMPLATE,
    STATUS_LIST_TITLE,
)


class StatusesList(LoginRequiredMixin, ListView):
    'Show the list of statuses.'
    model = Status
    template_name = STATUS_LIST_TEMPLATE
    context_object_name = 'statuses'

    def get_context_data(self, **kwargs):
        "Define the title."
        context = super().get_context_data(**kwargs)
        context[BUTTON_NAME_TITLE] = STATUS_LIST_TITLE
        return context


class CreateStatus(
    LoginRequiredMixin,
    SuccessMessageMixin,
    CreateView,
):
    'Create a status.'
    model = Status
    template_name = FORM_TEMPLATE
    form_class = StatusForm
    success_url = reverse_lazy('statuses:list')
    success_message = STATUS_CREATED

    def get_context_data(self, **kwargs):
        "Define the title and the button."
        context = super().get_context_data(**kwargs)
        context[BUTTON_NAME_TITLE] = CREATE_STATUS_TITLE
        context[BUTTON_TEXT] = CREATE_BUTTON
        return context


class ChangeStatus(
    LoginRequiredMixin,
    SuccessMessageMixin,
    UpdateView,
):
    'Change a status.'
    model = Status
    template_name = FORM_TEMPLATE
    form_class = StatusForm
    success_url = reverse_lazy('statuses:list')
    success_message = STATUS_CHANGED

    def get_context_data(self, **kwargs):
        "Define the title and the button."
        context = super().get_context_data(**kwargs)
        context[BUTTON_NAME_TITLE] = CHANGE_STATUS_TITLE
        context[BUTTON_TEXT] = CHANGE_BUTTON
        return context


class DeleteStatus(
    LoginRequiredMixin,
    FormValidMixin,
    DeleteView,
):
    'Delete a status.'
    model = Status
    template_name = DELETE_TEMPLATE
    success_url = reverse_lazy('statuses:list')

    def get_context_data(self, **kwargs):
        "Define the title and the button."
        context = super().get_context_data(**kwargs)
        context[BUTTON_NAME_TITLE] = DELETE_STATUS_TITLE
        context[BUTTON_TEXT] = DELETE_BUTTON
        return context
