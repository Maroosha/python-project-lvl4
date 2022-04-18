from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy
from .forms import CreateUserForm


class UserList(ListView):
    '.'
    template_name = 'users.html'
    model = User
    context_object_name = 'users'


    def get_context_data(self, **kwargs):
        '.'
        context = super().get_context_data(**kwargs)
        context['title'] = gettext_lazy('Users')
        return context


class CreateUser(CreateView, SuccessMessageMixin):
    '.'
    model = User
    template_name = 'form.html'
    form_class = CreateUserForm
    success_url = reverse_lazy('login')
    success_message = gettext_lazy('User successfully created.')


    def get_context_data(self, **kwargs):
        '.'
        context = super().get_context_data(**kwargs)
        context['title'] = gettext_lazy('Create user')
        context['button_text'] = gettext_lazy('Register')
        return context


class ChangeUser(UpdateView, SuccessMessageMixin):
    '.'
    model = User
    template_name = 'form.html'
    form_class = CreateUserForm
    success_url = reverse_lazy('users:list')
    success_message = gettext_lazy('User successfully changed.')


    def get_context_data(self, **kwargs):
        '.'
        context = super().get_context_data(**kwargs)
        context['title'] = gettext_lazy('Change user')
        context['button_text'] = gettext_lazy('Change')
        return context


class DeleteUser(DeleteView, SuccessMessageMixin):
    '.'
    model = User
    template_name = 'delete.html'
    success_url = reverse_lazy('users:list')
    success_message = gettext_lazy('User successfully deleted.')


    def get_context_data(self, **kwargs):
        '.'
        context = super().get_context_data(**kwargs)
        context['title'] = gettext_lazy('Delete user')
        context['button_text'] = gettext_lazy('Delete')
        return context
