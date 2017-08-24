from django import forms

from crispy_forms.bootstrap import AppendedText, Div
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit

from .models import Pessoa

class PessoaForm(forms.ModelForm):

    class Meta:
        model = Pessoa
        fields = ('nome', 'cpf', 'data_nasc')
        

    def __init__(self, *args, **kwargs):
        super(PessoaForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Div(
                'nome',
                'cpf',
                AppendedText('data_nasc', '<span class="fa fa-calendar"></span>'),
            ),
            Submit('salvar','Salvar', css_class = 'btn btn-success')
        )
    