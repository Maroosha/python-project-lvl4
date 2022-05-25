from django.db import models
from .constants import (
    STATUS_CREATED_AT,
    STATUS_NAME,
    VERBOSE_NAME,
    VERBOSE_NAME_PL,
)


class Status(models.Model):
    "Model for a status."
    name = models.CharField(
        max_length=100,
        null=False,
        verbose_name=STATUS_NAME,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=STATUS_CREATED_AT,
    )
    modified_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        """Method: when retrieving an object, the name is returned
        instead of just generic non-human readable text."""
        return self.name


    class Meta:
        "Meta class."
        verbose_name = VERBOSE_NAME
        verbose_name_plural = VERBOSE_NAME_PL
        ordering = ['id']
