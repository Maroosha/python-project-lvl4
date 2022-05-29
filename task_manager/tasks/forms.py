from django import forms
from .models import Task
from .constants import (
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
