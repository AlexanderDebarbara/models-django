from django.shortcuts import render
from django.views.generic import  ListView, CreateView, UpdateView, DeleteView
from .models import Pessoa, Endereco
from django.core.urlresolvers import reverse_lazy
from .forms import PessoaForm

class PessoaLista(ListView):    
    model = Pessoa

class PessoaAdd(CreateView):
    model = Pessoa
    success_url = reverse_lazy('pessoa:pessoa_list')    
    fields = ['nome', 'cpf', 'data_nasc']

class PessoaUpdate(UpdateView):
    model = Pessoa
    success_url = reverse_lazy('pessoa:pessoa_list')
    fields = ['nome', 'cpf', 'data_nasc']

class PessoaDelete(DeleteView):
    model = Pessoa
    success_url = reverse_lazy('pessoa:pessoa_list')

class EnderecoAdd(CreateView):
    model = Endereco
    success_url = reverse_lazy('pessoa:pessoa_list')
    fields = ['pessoa', 'logradouro', 'numero', 'complemento','cep']
    
def pessoa_new(request):
    form = PessoaForm
    return render(request, 'pessoa/pessoa_new.html', {'form': form})