from django import forms
from .models import Marks


class CreateNewMark(forms.Form):
    name = forms.CharField(label=' ')
    forms.TextInput
    class Meta:
            model = Marks
