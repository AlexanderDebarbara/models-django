from django.contrib import admin

from .models import Pessoa

class PessoaAdmin(admin.ModelAdmin):
   
    list_display = ("nome", "cpf", "data_nasc")

admin.site.register(Pessoa, PessoaAdmin)
