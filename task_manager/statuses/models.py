from django.db import models
from django.utils.translation import gettext_lazy


# http://www.learningaboutelectronics.com/Articles/verbose-name-and-verbose-name-plural-in-Django.php
class Status(models.Model):
    "Model for a status."
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
        verbose_name = gettext_lazy('Status')
        verbose_name_plural = gettext_lazy('Statuses')
        ordering = ['id']
