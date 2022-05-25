"Custom mixins for Users app."

from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect
from django.contrib import messages
from django.urls import reverse_lazy
from .constants import (
    CANT_CHANGE_ANOTHER_USER,
    LOGIN_REQUIRED,
)


class EditUserCustomMixin(AccessMixin):
    "Edit a user."
    success_url = reverse_lazy('users:list')

    def dispatch(self, request, *args, **kwargs):
        "Check if the user can edit/delete the given account."
        if kwargs['pk'] != self.request.user.id:
            messages.error(self.request, CANT_CHANGE_ANOTHER_USER)
            return redirect(self.success_url)
        return super().dispatch(request, *args, **kwargs)


class LoginRequiredCustomMixin(AccessMixin):
    """Custom mixin requiring authorized access.
    Shows custom message if not authorized."""
    error_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        "Set the mixin."
        if not request.user.is_authenticated:
            messages.error(self.request, LOGIN_REQUIRED)
            return redirect(self.error_url)
        return super().dispatch(request, *args, **kwargs)
