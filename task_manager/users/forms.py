from multiprocessing.spawn import import_main_path
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .constants import (
    FIRST_NAME,
    LAST_NAME,
    PASSWORD1,
    PASSWORD2,
    USERNAME,
)


class CreateUserForm(UserCreationForm):
    'User form.'
    class Meta:
        'User details.'
        User = get_user_model()
        model = User
        fields = [
            FIRST_NAME,
            LAST_NAME,
            USERNAME,
            PASSWORD1,
            PASSWORD2,
        ]
