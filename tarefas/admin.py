from .models import Tarefa
from django.contrib import admin

# Register your models here.
@admin.register(Tarefa)
class TarefaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'descricao', 'concluido',]