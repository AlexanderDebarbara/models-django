from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length = 200,verbose_name='Nome')
    cpf = models.CharField(max_length = 11, verbose_name='CPF')
    data_nasc = models.DateTimeField('Data de nascimento')

    def __str__(self):
        return self.nome    

class Endereco(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete = models.CASCADE, verbose_name = 'Pessoa')
    logradouro = models.CharField(max_length = 200, verbose_name = 'Logradouro')
    numero = models.CharField(max_length = 30, verbose_name= 'Numero')
    complemento = models.CharField(max_length = 200, verbose_name= 'Complemento')
    cep = models.CharField(max_length = 10, verbose_name = 'Cep')

    def __str__(self):
        return self.logradouro


class Prontuario(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete = models.CASCADE, verbose_name = 'Pessoa')
    city = models.CharField(max_length = 200, verbose_name= 'Cidade')
    macro_number = models.CharField(max_length = 200, verbose_name = 'Nº Macro')
    macro_read = models.CharField(max_length = 200, verbose_name = 'Leitura')
    pontual_macro = models.CharField(max_length = 200, verbose_name = 'Q = Pontual Macro')
    pontual_ultrasonico = models.CharField(max_length = 200, verbose_name = "Q = Pontual Ultrasonico")
    dn = models.CharField(max_length = 200, verbose_name = 'DN')
    marca = models.CharField(max_length = 200, verbose_name = 'Marca')
    entry_date = models.DateTimeField('Data de Entrada')
    observation = models.CharField(max_length = 200, verbose_name = 'Observação')    

    def __str__(self):
        return self.macro_number + " Leitura: " + self.macro_read


    