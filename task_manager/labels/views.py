from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import ProtectedError
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy
from .models import Label
from .forms import LabelForm


class LabelList(LoginRequiredMixin, ListView):
    "Show the list of labels."
    model = Label
    template_name = 'labels.html'
    context_object_name = 'labels'


    def get_context_data(self, **kwargs):
        "Define the title."
        context = super().get_context_data(**kwargs)
        context['title'] = gettext_lazy('Label')
        return context


class CreateLabel(
    LoginRequiredMixin,
    SuccessMessageMixin,
    CreateView,
):
    "Create a label."
    model = Label
    template_name = 'form.html'
    form_class = LabelForm
    success_url = reverse_lazy('labels:list')
    success_message = gettext_lazy('Label successfully created.')


    def get_context_data(self, **kwargs):
        "Define the title and the button."
        context = super().get_context_data(**kwargs)
        context['title'] = gettext_lazy('Create a Label')
        context['button_text'] = gettext_lazy('Create')
        return context


class ChangeLabel(
    LoginRequiredMixin,
    SuccessMessageMixin,
    UpdateView,
):
    "Change a label."
    model = Label
    template_name = 'form.html'
    form_class = LabelForm
    success_url = reverse_lazy('labels:list')
    success_message = gettext_lazy('Label successfully changed.')


    def get_context_data(self, **kwargs):
        "Define the title and the button."
        context = super().get_context_data(**kwargs)
        context['title'] = gettext_lazy('Change a label')
        context['button_text'] = gettext_lazy('Change')
        return context


class Deletelabel(
    LoginRequiredMixin,
    SuccessMessageMixin,
    DeleteView,
):
    "Delete a label."
    model = Label
    template_name = 'delete.html'
    success_url = reverse_lazy('labels:list')
    success_message = gettext_lazy('Label successfully deleted.')
    error_message = 'Cannot delete a label in use.'


    def form_valid(self, form):
        "Check if there are any tasks assigned to the given label."
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
        context['title'] = gettext_lazy('Delete a label')
        context['button_text'] = gettext_lazy('Delete')
        return context
