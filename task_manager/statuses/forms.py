from socket import fromshare
from django import forms
from .models import Status


class StatusForm(forms.ModelForm):
    'Status form.'
    class Meta:
        'Status details.'
        model = Status
        fields = [
            'name',
        ]
