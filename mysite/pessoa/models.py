from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length = 200,verbose_name='Nome')
    cpf = models.CharField(max_length = 11, verbose_name='CPF')
    data_nasc = models.DateTimeField('Data de nascimento')

    def __str__(self):
        return self.nome    

class Endereco(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete = models.CASCADE)
    logradouro = models.CharField(max_length = 200)
    numero = models.CharField(max_length = 30)
    complemento = models.CharField(max_length = 200)
    cep = models.CharField(max_length = 10)

    def __str__(self):
        return self.logradouro