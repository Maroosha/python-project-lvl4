from django.db import models
from django.utils.translation import gettext_lazy


class Label(models.Model):
    "Model for a label."
    name = models.CharField(
        max_length=100,
        null=False,
        verbose_name=gettext_lazy('Name'),
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=gettext_lazy('Created at'),
    )
    modified_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        """Method: when retrieving an object, the name is returned
        instead of just generic non-human readable text."""
        return self.name


    class Meta:
        "Meta class."
        verbose_name = gettext_lazy('Label')
        verbose_name_plural = gettext_lazy('Labels')
        ordering = ['id']
