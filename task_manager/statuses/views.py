from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy
from .models import Status
from .forms import StatusForm


class StatusesList(LoginRequiredMixin, ListView):
    'Show the list of statuses.'
    model = Status
    template_name = 'statuses.html'
    context_object_name = 'statuses'

    def get_context_data(self, **kwargs):
        '.'
        context = super().get_context_data(**kwargs)
        context['title'] = gettext_lazy('Statuses')
        return context


class CreateStatus(
    LoginRequiredMixin,
    SuccessMessageMixin,
    CreateView,
):
    'Create a status.'
    model = Status
    template_name = 'form.html'
    form_class = StatusForm
    success_url = reverse_lazy('statuses:list')
    success_message = gettext_lazy('Status successfully created.')


    def get_context_data(self, **kwargs):
        '.'
        context = super().get_context_data(**kwargs)
        context['title'] = gettext_lazy('Create a status')
        context['button_text'] = gettext_lazy('Create')
        return context


class ChangeStatus(
    LoginRequiredMixin,
    SuccessMessageMixin,
    UpdateView,
):
    'Change a status.'
    model = Status
    template_name = 'form.html'
    form_class = StatusForm
    success_url = reverse_lazy('statuses:list')
    success_message = gettext_lazy('Status successfully changed.')


    def get_context_data(self, **kwargs):
        '.'
        context = super().get_context_data(**kwargs)
        context['title'] = gettext_lazy('Change a status')
        context['button_text'] = gettext_lazy('Change')
        return context


class DeleteStatus(
    LoginRequiredMixin,
    SuccessMessageMixin,
    DeleteView,
):
    'Delete a status.'
    model = Status
    template_name = 'delete.html'
    success_url = reverse_lazy('statuses:list')
    success_message = gettext_lazy('Status successfully deleted.')


    def get_context_data(self, **kwargs):
        '.'
        context = super().get_context_data(**kwargs)
        context['title'] = gettext_lazy('Delete a status')
        context['button_text'] = gettext_lazy('Delete')
        return context
