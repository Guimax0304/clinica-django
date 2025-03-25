# agendamentos/urls.py

from django.urls import path
from agendamentos import views
from .views import (
    ListarAgendamentosView,
    CriarAgendamentoView,
    EditarAgendamentoView,
    DeletarAgendamentoView,
    EventosJsonView,
    DetalhesAgendamentoView,
    ExcluirAgendamentoAjaxView,
)


app_name = 'agendamentos'

urlpatterns = [
    path('', ListarAgendamentosView.as_view(), name='listar_agendamentos'),
    path('criar/', CriarAgendamentoView.as_view(), name='criar_agendamento'),
    path('editar/<int:pk>/', EditarAgendamentoView.as_view(), name='editar_agendamento'),
    path('deletar/<int:pk>/', DeletarAgendamentoView.as_view(), name='deletar_agendamento'),
    path('eventos-json/', EventosJsonView.as_view(), name='eventos_json'),
    path('detalhes/<int:pk>/', DetalhesAgendamentoView.as_view(), name='detalhes_agendamento'),
    path('ajax/deletar/<int:pk>/', ExcluirAgendamentoAjaxView.as_view(), name='ajax_excluir_agendamento'),
]
