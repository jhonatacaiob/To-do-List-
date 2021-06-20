from django.shortcuts import redirect, render
from .models import Tarefa
from .forms import TarefaModelForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required



# Create your views here.
@login_required
def index(request):
    if(str(request.method) == 'GET'):
        tarefas = Tarefa.objects.all()
        context = {
            'tarefas': Tarefa.objects.all()
        }
        return render(request, 'tarefas/tarefas.html', context)



@login_required
def cadastro(request):
    tarefas = Tarefa.objects.all()
    if(str(request.method) == 'GET'):
        form = TarefaModelForm()
        context = {

            'form': form,
            'tarefas': tarefas
        }
        return render(request, 'tarefas/cadastro.html', context)


    elif(str(request.method) == 'POST'):
        form = TarefaModelForm(request.POST)
        if(form.is_valid()):
            form.save()

            return redirect(to= 'index')
        
        else:

            form = TarefaModelForm()
            return render(request, 'tarefas/cadastro.html')

@login_required
def atualizar(request, id):
    tarefas = Tarefa.objects.all()
    form = TarefaModelForm(request.POST or None, instance = Tarefa.objects.get(pk = id))
    
    if(str(request.method) == "GET"):
        context = {
            'tarefas': tarefas,
            'form': form,
            'id': id,
        }
        return render(request, 'tarefas/atualizar.html', context)

    elif(str(request.method) == 'POST'):
        if(form.is_valid()):
            form.save()
        return redirect(to='index')


@login_required
def excluir(request, id):
    tarefa = Tarefa.objects.get(pk = id)
    tarefa.delete()
    return redirect(to='index')