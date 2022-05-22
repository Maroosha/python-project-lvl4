from django import forms
from .models import Status
from .constants import STATUS_NAME


class StatusForm(forms.ModelForm):
    'Status form.'
    class Meta:
        'Status details.'
        model = Status
        fields = [
            STATUS_NAME,
        ]
