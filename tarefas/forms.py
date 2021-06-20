from django import forms
from .models import Tarefa



class TarefaModelForm(forms.ModelForm):
    
    class Meta:
        model = Tarefa
        fields = ['nome', 'descricao', 'concluido'  ]