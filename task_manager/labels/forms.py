from django import forms
from .models import Label
from .constants import NAME


class LabelForm(forms.ModelForm):
    'Label form.'
    class Meta:
        'Label details.'
        model = Label
        fields = [
            NAME,
        ]
