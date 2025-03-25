from django.urls import path
from . import views

app_name = 'salas'

urlpatterns = [
    path('', views.listar_salas, name='listar_salas'),
    path('criar/', views.criar_sala, name='criar_sala'),
    path('editar/<int:id>/', views.editar_sala, name='editar_sala'),
    path('deletar/<int:id>/', views.deletar_sala, name='deletar_sala'),
]
