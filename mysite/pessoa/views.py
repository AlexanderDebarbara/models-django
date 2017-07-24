from django.shortcuts import render
from django.views import generic
from .models import Pessoa
from django.core.urlresolvers import reverse_lazy


class PessoaLista(generic.ListView):    
    model = Pessoa

class PessoaAdd(generic.CreateView):    
    model = Pessoa
    success_url = reverse_lazy('pessoa:pessoa_list')
    fields = ['nome', 'cpf', 'data_nasc']

class PessoaUpdate(generic.UpdateView):
    model = Pessoa
    success_url = reverse_lazy('pessoa:pessoa_list')
    fields = ['nome', 'cpf', 'data_nasc']

class PessoaDelete(generic.DeleteView):
    model = Pessoa
    success_url = reverse_lazy('pessoa:pessoa_list')
