from django.shortcuts import render
from .models import TURMA, PROJETO, EIXO
def index(request):

    projetos = PROJETO.objects.all()

    contexto={'projetos': []}
    
    for projeto in projetos: 
        id = projeto.id
        nome = projeto.nome_projeto
        capa = projeto.foto_capa
        eixo = projeto.eixo.nome
        descricao = projeto.descricao
        contexto['projetos'].append({'id': id,'nome_projeto':nome,'foto_capa':capa, 'descricao': descricao, 'eixo': eixo }) 
        

    return  render(request, 'index.html', contexto) 

def details(request):
    return render(request, 'detalhes.hmtl')

def login(request):
    return render(request, 'login.html')

def admin(request):
    return render(request, 'admin.html')

def eixo(request):
    return render(request, 'eixo.html')

def cadastro(request):
    return render(request, 'cadastro.html')