from django import forms
from .models import Label


class LabelForm(forms.ModelForm):
    'Label form.'
    class Meta:
        'Label details.'
        model = Label
        fields = [
            'name',
        ]
