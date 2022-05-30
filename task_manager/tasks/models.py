from django.db import models
from task_manager.statuses.models import Status
from task_manager.labels.models import Label
from django.contrib.auth import get_user_model
from .constants import (
    TASK_CREATED_AT,
    TASK_CREATED_BY,
    TASK_DESCRIPTION,
    TASK_EXECUTIVE,
    TASK_LABEL,
    TASK_NAME,
    TASK_STATUS,
    VERBOSE_NAME,
    VERBOSE_NAME_PL,
)

User = get_user_model()


class Task(models.Model):
    "Model for a task."
    name = models.CharField(  # max < 255 symbols
        max_length=100,
        null=False,
        verbose_name=TASK_NAME,
    )
    description = models.TextField(
        verbose_name=TASK_DESCRIPTION,
    )
    status = models.ForeignKey(
        Status,
        on_delete=models.PROTECT,
        null=True,
#        related_name=TASK_STATUS,
        related_name='task_status',
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        null=False,
#        related_name=TASK_CREATED_BY,
        related_name='task_created_by',
    )
    executive = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        null=True,
#        related_name=TASK_EXECUTIVE,
        related_name='task_executive',
    )
    labels = models.ManyToManyField(
        Label,
        related_name=TASK_LABEL,
        blank=True,
        through='TaskLabelRelation',
        through_fields=('task', 'label'),
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=TASK_CREATED_AT,
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


class TaskLabelRelation(models.Model):
    "Task to label relationship table."
    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
    )
    label = models.ForeignKey(
        Label,
        on_delete=models.PROTECT,
    )
