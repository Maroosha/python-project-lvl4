from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import ProtectedError
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy
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
    ERROR_STATUS_IN_USE,
    FORM_TEMPLATE,
    STATUS_CHANGED,
    STATUS_CREATED,
    STATUS_DELETED,
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
        context[BUTTON_NAME_TITLE] = gettext_lazy(STATUS_LIST_TITLE)
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
    success_message = gettext_lazy(STATUS_CREATED)


    def get_context_data(self, **kwargs):
        "Define the title and the button."
        context = super().get_context_data(**kwargs)
        context[BUTTON_NAME_TITLE] = gettext_lazy(CREATE_STATUS_TITLE)
        context[BUTTON_TEXT] = gettext_lazy(CREATE_BUTTON)
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
    success_message = gettext_lazy(STATUS_CHANGED)


    def get_context_data(self, **kwargs):
        "Define the title and the button."
        context = super().get_context_data(**kwargs)
        context[BUTTON_NAME_TITLE] = gettext_lazy(CHANGE_STATUS_TITLE)
        context[BUTTON_TEXT] = gettext_lazy(CHANGE_BUTTON)
        return context


class DeleteStatus(
    LoginRequiredMixin,
    SuccessMessageMixin,
    DeleteView,
):
    'Delete a status.'
    model = Status
    template_name = DELETE_TEMPLATE
    success_url = reverse_lazy('statuses:list')
    success_message = gettext_lazy(STATUS_DELETED)
    error_message = gettext_lazy(ERROR_STATUS_IN_USE)


    def form_valid(self, form):
        "Check if there are any tasks assigned to the given status."
        try:
            self.object.delete()
        except ProtectedError:
            messages.error(self.request, self.error_message)
        else:
            messages.success(self.request, self.success_message)
        return HttpResponseRedirect(self.success_url)


    def get_context_data(self, **kwargs):
        "Define the title and the button."
        context = super().get_context_data(**kwargs)
        context[BUTTON_NAME_TITLE] = gettext_lazy(DELETE_STATUS_TITLE)
        context[BUTTON_TEXT] = gettext_lazy(DELETE_BUTTON)
        return context
