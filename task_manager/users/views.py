from django.contrib import messages
from django.contrib.auth.mixins import AccessMixin, LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import ProtectedError
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy
from .forms import CreateUserForm
from django.contrib.auth import get_user_model


User = get_user_model()


class EditUserMixin(AccessMixin):
    "Edit an account."
    error_message = gettext_lazy('You do not have a permission to \
change another user.')
    success_url = reverse_lazy('users:list')


    def dispatch(self, request, *args, **kwargs):
        "Check if the user can edit/delete the given account."
        print(f'kwargs = {kwargs}')
        print(f'self.request.user.id = {self.request.user.id}')
        if kwargs['pk'] != self.request.user.id:
            messages.error(self.request, self.error_message)
            return redirect(self.success_url)
        return super().dispatch(request, *args, **kwargs)


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
        context['title'] = gettext_lazy('Create a user')
        context['button_text'] = gettext_lazy('Register')
        return context


class ChangeUser(
    LoginRequiredMixin,
    EditUserMixin,
    SuccessMessageMixin,
    UpdateView,
):
    '.'
    model = User
    template_name = 'form.html'
    form_class = CreateUserForm
    success_url = reverse_lazy('users:list')
    success_message = gettext_lazy('User successfully changed.')


    def get_context_data(self, **kwargs):
        '.'
        context = super().get_context_data(**kwargs)
        context['title'] = gettext_lazy('Change a user')
        context['button_text'] = gettext_lazy('Change')
        return context


class DeleteUser(
    LoginRequiredMixin,
    SuccessMessageMixin,
    EditUserMixin,
    DeleteView,
):
    '.'
    model = User
    template_name = 'delete.html'
    success_url = reverse_lazy('users:list')
    success_message = gettext_lazy('User successfully deleted.')


    def get_context_data(self, **kwargs):
        '.'
        context = super().get_context_data(**kwargs)
        context['title'] = gettext_lazy('Delete a user')
        context['button_text'] = gettext_lazy('Delete')
        return context


    def form_valid(self, form):
        "Check if any statuses or tasks are assigned to the given user."
        try:
            self.object.delete()
        except ProtectedError:
            error_user_in_use = 'Cannot delete a user in use.'
            messages.error(self.request, error_user_in_use)
        else:
            messages.success(self.request, self.success_message)
        return HttpResponseRedirect(self.success_url)
