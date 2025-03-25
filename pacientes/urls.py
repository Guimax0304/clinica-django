#pacientes/urls.py

from django.urls import path
from . import views

app_name = 'pacientes'

urlpatterns = [
    # Páginas HTML
    path('', views.listar_pacientes, name='listar_pacientes'),  # Página inicial para listar pacientes
    path('criar/', views.criar_paciente, name='criar_paciente'),  # Página para criar paciente
    path('editar/<int:id>/', views.editar_paciente, name='editar_paciente'),  # Página para editar paciente
    path('deletar/<int:id>/', views.deletar_paciente, name='deletar_paciente'),  # Página para deletar paciente
    
    # APIs para AJAX
    path('api/listar/', views.api_listar_pacientes, name='api_listar_pacientes'),  # API para listar pacientes
    path('api/criar/', views.api_criar_paciente, name='api_criar_paciente'),  # API para criar paciente
    path('api/editar/<int:id>/', views.api_editar_paciente, name='api_editar_paciente'),  # API para editar paciente
    path('api/deletar/<int:id>/', views.api_deletar_paciente, name='api_deletar_paciente'),  # API para deletar paciente
]
