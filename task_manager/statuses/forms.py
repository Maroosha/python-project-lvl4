from django import forms
from .models import Status
from .constants import NAME


class StatusForm(forms.ModelForm):
    'Status form.'
    class Meta:
        'Status details.'
        model = Status
        fields = [
            NAME,
        ]
