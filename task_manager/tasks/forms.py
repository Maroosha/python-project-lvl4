from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    'Task form.'
    class Meta:
        'Task details.'
        model = Task
        fields = [
            'name',
            'description',
            'status',
            'created_by',
            'executive',
        ]
