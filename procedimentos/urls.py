# Procedimentos/urls.py

from django.urls import path
from . import views

app_name = 'procedimentos'

urlpatterns = [
    # Rota para listar todos os procedimentos
    path('', views.listar_procedimentos, name='listar_procedimentos'),

    # Rota para criar um novo procedimento
    path('criar/', views.criar_procedimento, name='criar_procedimento'),

    # Rota para editar um procedimento existente
    path('editar/<int:id>/', views.editar_procedimento, name='editar_procedimento'),

    # Rota para deletar um procedimento
    path('deletar/<int:id>/', views.deletar_procedimento, name='deletar_procedimento'),
]
