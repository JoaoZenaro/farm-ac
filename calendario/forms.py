from dataclasses import fields
from django import forms
from prestacao.models import Prestacao

class CalendarioForm(forms.ModelForm):
    class Meta:
        model = Prestacao
        fields = ('data',)
