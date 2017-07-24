from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length = 200)
    cpf = models.CharField(max_length = 11)
    data_nasc = models.DateTimeField('Data de nascimento')

    def __str__(self):
        return self.nome    

