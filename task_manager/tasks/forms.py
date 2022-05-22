from django import forms
from django.utils.translation import gettext_lazy
from .models import Task
from .constants import (
    CREATED_BY,
    DESCRIPTION,
    EXECUTIVE,
    LABEL,
    NAME,
    STATUS,
    TASK_DESCRIPTION,
    TASK_EXECUTIVE,
    TASK_LABEL,
    TASK_NAME,
    TASK_STATUS,
)


class TaskForm(forms.ModelForm):
    'Task form.'
    class Meta:
        'Task details.'
        model = Task
        fields = [
            NAME,
            DESCRIPTION,
            STATUS,
            CREATED_BY,
            EXECUTIVE,
            LABEL,
        ]
        label = {
            NAME: gettext_lazy(TASK_NAME),
            DESCRIPTION: gettext_lazy(TASK_DESCRIPTION),
            STATUS: gettext_lazy(TASK_STATUS),
            EXECUTIVE: gettext_lazy(TASK_EXECUTIVE),
            LABEL: gettext_lazy(TASK_LABEL),
        }
