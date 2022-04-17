from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.utils.translation import gettext_lazy


class IndexPage(TemplateView):
    '.'
    template_name = "index.html"


class Login(LoginView):
    '.'
    template_name = 'form.html'
    success_message = gettext_lazy('Logged in successfully.')


    def get_context_data(self, **kwargs):
        '.'
        context = super().get_context_data(**kwargs)
        context['title'] = gettext_lazy('Log in')
        context['button_text'] = gettext_lazy('Log in')
        context['value'] = 'login'
        return context


class Logout(LogoutView):
    '.'


    def dispatch(self, request, *args, **kwargs):
        '.'
        messages.add_message(request, messages.INFO, gettext_lazy('Logged out successfully.'))
        return super().dispatch(request, *args, **kwargs)
