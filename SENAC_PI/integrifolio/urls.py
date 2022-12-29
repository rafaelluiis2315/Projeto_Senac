from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('detalhes/<int:id>', views.details),
    path('login', views.login),
    path('admin',views.admin),
    path('admin/eixo',views.eixo),
    path('cadastro',views.cadastro),
]
