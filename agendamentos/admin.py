#agendamento/admin.py

from django.contrib import admin
from .models import Agendamento, Sala

# Registro de Agendamento
@admin.register(Agendamento)
class AgendamentoAdmin(admin.ModelAdmin):
    list_display = ('id', 'paciente', 'profissional', 'data_inicio', 'data_fim', 'procedimento')
    list_filter = ('profissional', 'data_inicio', 'procedimento',)
    search_fields = ('paciente__nome', 'profissional__nome', 'descricao')
    ordering = ('-data_inicio',)

# Registro de Sala
@admin.register(Sala)
class SalaAdmin(admin.ModelAdmin):
    list_display = ('id', 'numero', 'descricao')
    search_fields = ('numero', 'descricao')
