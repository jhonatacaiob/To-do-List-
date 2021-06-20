from django.db import models

# Create your models here.

class Tarefa(models.Model):
    criado = models.DateTimeField('Data de criação', auto_now_add=True)
    nome = models.CharField('Nome', max_length=100)
    descricao = models.CharField('Descricao', max_length=255, blank = True)
    concluido = models.BooleanField("Concluido", default=False)

    def __str__(self):
        return self.nome