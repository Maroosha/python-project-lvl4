# from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
# from django.shortcuts import redirect
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy
from .forms import CreateUserForm
from django.contrib.auth import get_user_model


User = get_user_model()


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


class CreateUser(SuccessMessageMixin, CreateView):
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


class ChangeUser(
    LoginRequiredMixin,
    SuccessMessageMixin,
    UpdateView,
):
    '.'
    model = User
    template_name = 'form.html'
    form_class = CreateUserForm
    success_url = reverse_lazy('users:list')
    success_message = gettext_lazy('User successfully changed.')
    error_message = gettext_lazy('You do not have a permission to \
change another user.')


    def get_context_data(self, **kwargs):
        '.'
        context = super().get_context_data(**kwargs)
        context['title'] = gettext_lazy('Change user')
        context['button_text'] = gettext_lazy('Change')
        # forbid a user to change anyone else's account
#        if request.user != self.get_object():
#            messages.error(
#                self.request, self.error_message,
#            )
#            return redirect('users:list')
        return context


class DeleteUser(
    LoginRequiredMixin,
    SuccessMessageMixin,
    DeleteView,
):
    '.'
    model = User
    template_name = 'delete.html'
    success_url = reverse_lazy('users:list')
    success_message = gettext_lazy('User successfully deleted.')
    error_message = gettext_lazy('You do not have a permission to \
change another user.')


    def get_context_data(self, **kwargs):
        '.'
        context = super().get_context_data(**kwargs)
        context['title'] = gettext_lazy('Delete user')
        context['button_text'] = gettext_lazy('Delete')
        # forbid a user deleting anyone else's account
#        if request.user != self.get_object():
#            messages.error(
#                self.request, self.error_message,
#            )
#            return redirect('users:list')
        return context
