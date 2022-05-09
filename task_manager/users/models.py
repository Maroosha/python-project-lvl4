# from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy

class User(AbstractUser):
    "User class."


    def __str__(self):
        return self.get_full_name()


    class Meta:
        'User class details.'
        verbose_name = gettext_lazy('User')
        verbose_name_plural = gettext_lazy('Users')
        ordering = ['id']
