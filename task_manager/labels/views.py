from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.urls import reverse_lazy
from task_manager.custom_mixins import FormValidMixin
from .models import Label
from .forms import LabelForm
from .constants import (
    BUTTON_NAME_TITLE,
    BUTTON_TEXT,
    CHANGE_BUTTON,
    CREATE_BUTTON,
    CHANGE_LABEL_TITLE,
    CREATE_LABEL_TITLE,
    DELETE_BUTTON,
    DELETE_TEMPLATE,
    DELETE_LABEL_TITLE,
    FORM_TEMPLATE,
    LABEL_CHANGED,
    LABEL_CREATED,
    LABEL_LIST_TEMPLATE,
    LABEL_LIST_TITLE,
)


class LabelList(LoginRequiredMixin, ListView):
    "Show the list of labels."
    model = Label
    template_name = LABEL_LIST_TEMPLATE
    context_object_name = 'labels'

    def get_context_data(self, **kwargs):
        "Define the title."
        context = super().get_context_data(**kwargs)
        context[BUTTON_NAME_TITLE] = LABEL_LIST_TITLE
        return context


class CreateLabel(
    LoginRequiredMixin,
    SuccessMessageMixin,
    CreateView,
):
    "Create a label."
    model = Label
    template_name = FORM_TEMPLATE
    form_class = LabelForm
    success_url = reverse_lazy('labels:list')
    success_message = LABEL_CREATED

    def get_context_data(self, **kwargs):
        "Define the title and the button."
        context = super().get_context_data(**kwargs)
        context[BUTTON_NAME_TITLE] = CREATE_LABEL_TITLE
        context[BUTTON_TEXT] = CREATE_BUTTON
        return context


class ChangeLabel(
    LoginRequiredMixin,
    SuccessMessageMixin,
    UpdateView,
):
    "Change a label."
    model = Label
    template_name = FORM_TEMPLATE
    form_class = LabelForm
    success_url = reverse_lazy('labels:list')
    success_message = LABEL_CHANGED

    def get_context_data(self, **kwargs):
        "Define the title and the button."
        context = super().get_context_data(**kwargs)
        context[BUTTON_NAME_TITLE] = CHANGE_LABEL_TITLE
        context[BUTTON_TEXT] = CHANGE_BUTTON
        return context


class Deletelabel(
    LoginRequiredMixin,
    FormValidMixin,
    DeleteView,
):
    "Delete a label."
    model = Label
    template_name = DELETE_TEMPLATE
    success_url = reverse_lazy('labels:list')

    def get_context_data(self, **kwargs):
        "Define the title and the button."
        context = super().get_context_data(**kwargs)
        context[BUTTON_NAME_TITLE] = DELETE_LABEL_TITLE
        context[BUTTON_TEXT] = DELETE_BUTTON
        return context
