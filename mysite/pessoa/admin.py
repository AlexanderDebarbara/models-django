from django.contrib import admin

from .models import Pessoa, Endereco

class PessoaAdmin(admin.ModelAdmin):
   
    list_display = ("nome", "cpf", "data_nasc")

admin.site.register(Pessoa, PessoaAdmin)
admin.site.register(Endereco)
