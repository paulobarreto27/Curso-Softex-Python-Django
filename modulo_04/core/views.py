from django.shortcuts import render
from django.http import HttpResponse
from .models import Tarefa
from .models import Execucao

# Create your views here.
def home(request):
    todas_as_tarefas = Tarefa.objects.all()
    todas_as_execucoes = Execucao.objects.all()
    context = {
        'nome_usuario': 'Paulo Barreto',
        'tecnologias': ['Python','Django','HTML','CSS'],
        'tarefas': todas_as_tarefas,
        'execucoes': todas_as_execucoes
    }
    #return HttpResponse("<h1>Olá, Mundo! Está é a minha primeira página Django!</h1>")
    return render(request, 'home.html', context)
def login(request):
    return HttpResponse("<input>Login</input>")

def serviços(request):
    return HttpResponse("<h1>Nossos Seviços</h1>")