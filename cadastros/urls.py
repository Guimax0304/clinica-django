# cadastros/urls.py
from django.urls import path
from . import views

app_name = 'cadastros'

urlpatterns = [
    path('', views.cadastros_view, name='cadastros'),
    path('criar/', views.criar_cadastro, name='criar_cadastro'),
    path('listar/', views.listar_cadastros, name='listar_cadastros'),
    path('editar/<int:pk>/', views.editar_cadastro, name='editar_cadastro'),
    path('deletar/<int:pk>/', views.deletar_cadastro, name='deletar_cadastro'),
]
