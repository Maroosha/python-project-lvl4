from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from .constants import (
    BUTTON_TEXT,
    FORM_TEMPLATE,
    INDEX_TEMPLATE,
    LOGGED_IN,
    LOGIN_VALUE,
    LOGGED_OUT,
)


class IndexPage(TemplateView):
    "Main page."
    template_name = INDEX_TEMPLATE


class Login(SuccessMessageMixin, LoginView):
    "Log in into Task Manager."
    template_name = FORM_TEMPLATE
    success_message = LOGGED_IN

    def get_context_data(self, **kwargs):
        "Set up buttons."
        context = super().get_context_data(**kwargs)
        context[BUTTON_TEXT] = LOGIN_VALUE
        return context


class Logout(SuccessMessageMixin, LogoutView):
    "Log out from Task Manager."

    def dispatch(self, request, *args, **kwargs):
        "Log out and show a logout message."
        messages.add_message(request, messages.INFO, LOGGED_OUT)
        return super().dispatch(request, *args, **kwargs)
