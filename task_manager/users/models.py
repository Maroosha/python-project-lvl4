# from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy

class User(AbstractUser):
    pass


    class Meta:
        '.'
        verbose_name = gettext_lazy('User')
        verbose_name_plural = gettext_lazy('Users')
        ordering = ['id']
