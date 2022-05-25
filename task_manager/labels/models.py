from django.db import models
from .constants import (
    LABEL_CREATED_AT,
    LABEL_NAME,
    VERBOSE_NAME,
    VERBOSE_NAME_PL,
)


class Label(models.Model):
    "Model for a label."
    name = models.CharField(
        max_length=100,
        null=False,
        verbose_name=LABEL_NAME,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=LABEL_CREATED_AT,
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
