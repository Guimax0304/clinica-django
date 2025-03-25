#profissionai/urls.py

from django.urls import path
from . import views

app_name = 'profissionais'

urlpatterns = [
    # URL para listar todos os profissionais
    path('', views.listar_profissionais, name='listar_profissionais'),

    # URL para criar um novo profissional
    path('criar/', views.criar_profissional, name='criar_profissional'),

    # URL para editar um profissional existente
    path('editar/<int:id>/', views.editar_profissional, name='editar_profissional'),

    # URL para deletar um profissional
    path('deletar/<int:id>/', views.deletar_profissional, name='deletar_profissional'),
]
