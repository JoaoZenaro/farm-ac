from django import forms
from .models import Lancamentos

class LancamentoForm(forms.ModelForm):

    class Meta:
        model = Lancamentos
        fields = ('nome','descricao','tipo','prestacao','valor','data')
        labels = {
            'fullname':'Nome',
            'descricao':'Descrição'
        }

        widgets = {
            'data': forms.DateInput(),
            'valor': forms.NumberInput()
        }

    def __init__(self, *args, **kwargs):
        super(LancamentoForm,self).__init__(*args, **kwargs)
        self.fields['tipo'].empty_label = "Selecione"
        self.fields['prestacao'].empty_label = "Selecione"
        # self.fields['emp_code'].required = False
