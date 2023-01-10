from django.shortcuts import render, get_object_or_404
from .models import TURMA, PROJETO, EIXO
def index(request):
    
    query = request.GET.get('busca')

    if query:
        projeto = PROJETO.objects.filter(nome_projeto__icontains=query)

        projetos_list = []
        
        for p in projeto: 
            id = p.id
            curso = p.id_turma.curso.tipo_curso.nome
            nome = p.nome_projeto
            numero_turma = p.id_turma.numero_turma
            capa = p.foto_capa
            eixo = p.eixo.nome
            projetos_list.append({'id': id, 'curso': curso, 'nome_projeto':nome,'numero_turma': numero_turma ,'foto_capa':capa, 'eixo': eixo }) 
    else:

        projetos = PROJETO.objects.all()

        projetos_list = []
        
        for projeto in projetos: 
            id = projeto.id
            curso = projeto.id_turma.curso.tipo_curso.nome
            nome = projeto.nome_projeto
            numero_turma = projeto.id_turma.numero_turma
            capa = projeto.foto_capa
            eixo = projeto.eixo.nome
            projetos_list.append({'id': id, 'curso': curso, 'nome_projeto':nome,'numero_turma': numero_turma ,'foto_capa':capa, 'eixo': eixo }) 

    destaques = PROJETO.objects.filter(destaque="v")
        
    return  render(request, 'index.html', {'projetos': projetos_list, 'destaques': destaques}) 

def details(request,id):
    projeto = get_object_or_404(PROJETO,id=id)
    return render(request, 'detalhes.html', {'projeto':projeto})

def login(request):
    return render(request, 'login.html')

def admin(request):
    return render(request, 'admin.html')

def eixo(request):
    return render(request, 'eixo.html')

def cadastro(request):
    return render(request, 'cadastro.html')

def sobre(request):
    return render(request,'sobre.html')