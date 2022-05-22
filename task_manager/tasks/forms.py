from django import forms
from django.utils.translation import gettext_lazy
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
            'label',
        ]
        label = {
            'name': gettext_lazy('Name'),
            'description': gettext_lazy('Description'),
            'status': gettext_lazy('Status'),
            'executive': gettext_lazy('Executive'),
            'label': gettext_lazy('Label'),
        }
