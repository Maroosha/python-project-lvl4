from django.contrib.auth.models import AbstractUser
from .constants import (
    VERBOSE_NAME,
    VERBOSE_NAME_PL,
)

class User(AbstractUser):
    "User class."


    def __str__(self):
        return self.get_full_name()


    class Meta:
        'User class details.'
        verbose_name = VERBOSE_NAME
        verbose_name_plural = VERBOSE_NAME_PL
        ordering = ['id']
