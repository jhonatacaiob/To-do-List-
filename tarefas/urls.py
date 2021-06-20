from django.urls import path
from .views import atualizar, index, cadastro, excluir

urlpatterns = [
    path('tarefas', index, name = 'index'),
    path('cadastro', cadastro, name = 'cadastro'),
    path('atualizar/<int:id>', atualizar, name = 'atualizar'),
    path('excluir/<int:id>', excluir, name = 'excluir'),

]
