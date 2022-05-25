from django import forms
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
            NAME: TASK_NAME,
            DESCRIPTION: TASK_DESCRIPTION,
            STATUS: TASK_STATUS,
            EXECUTIVE: TASK_EXECUTIVE,
            LABEL: TASK_LABEL,
        }
