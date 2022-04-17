# from dataclasses import fields
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    'User form.'
    class Meta:
        'User details.'
        model = User
        fields = [
            'first_name',
            'last_name',
            'login',
            'password',
            'password_confirmation',
        ]
