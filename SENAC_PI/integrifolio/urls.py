from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='Home'),
    path('detalhes/<int:id>', views.details, name='Detalhes'),
    path('login', views.login, name='Login'),
    path('admin',views.admin, name='Admin'),
    path('eixo',views.eixo, name='Eixo'),
    path('cadastro',views.cadastro, name='Cadastro'),
]
