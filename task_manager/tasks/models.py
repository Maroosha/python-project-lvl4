from django.db import models
from task_manager.statuses.models import Status
from task_manager.labels.models import Label
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy

User = get_user_model()


class Task(models.Model):
    "Model for a task."
    name = models.CharField(  # max < 255 symbols
        max_length=100,
        null=False,
        verbose_name=gettext_lazy('Name'),
    )
    description = models.TextField(
        verbose_name=gettext_lazy('Description'),
    )
    status = models.ForeignKey(
        Status,
        on_delete=models.PROTECT,
        null=True,
        related_name='Status',
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        null=False,
        related_name='Created_by',
    )
    executive = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        null=True,
        related_name='Executive',
    )
    labels = models.ManyToManyField(
        Label,
        related_name='Label',
        blank=True,
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
        verbose_name = gettext_lazy('Task')
        verbose_name_plural = gettext_lazy('Tasks')
        ordering = ['id']
