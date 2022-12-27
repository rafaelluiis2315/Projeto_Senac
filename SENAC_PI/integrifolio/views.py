from django.shortcuts import render

def index(request): 
    return  render(request, 'index.html') 

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