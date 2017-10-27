from django import forms

from crispy_forms.bootstrap import AppendedText, Div
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit

from .models import Pessoa, Endereco, Prontuario

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

class EnderecoForm(forms.ModelForm):

    class Meta:
        model = Endereco
        fields = ('pessoa', 'logradouro', 'numero', 'complemento','cep')

    def __init__(self, *args, **kwargs):
        super(EnderecoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Div(
                'pessoa',
                'logradouro',
                'numero',
                'complemento',
                'cep',
            ),
            Submit('salvar', 'Salvar', css_class = 'btn btn-success')
        )

class ProntuarioForm(forms.ModelForm):
    
    class Meta:
        model = Prontuario
        fields = ('pessoa', 'city', 'macro_number', 'macro_read', 'pontual_macro', 'pontual_ultrasonico', 'dn', 'marca', 'entry_date', 'observation')

    def __init__(self, *args, **kwargs):
        super(ProntuarioForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Div('pessoa', 
                'city', 
                'macro_number', 
                'macro_read', 
                'pontual_macro', 
                'pontual_ultrasonico', 
                'dn', 
                'marca', 
                AppendedText('entry_date', '<span class="fa fa-calendar"></span>'),
                'observation',                
            ),
            Submit('salvar', 'Salvar', css_class = 'btn btn-success')
        )