#pacientes/admin.py

from django.contrib import admin
from .models import Paciente


def marcar_como_ativo(self, request, queryset):
    queryset.update(ativo=True)
    self.message_user(request, f"{queryset.count()} pacientes marcados como ativos.")

marcar_como_ativo.short_description = "Marcar como Ativo"

@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    actions = [marcar_como_ativo]
    list_display = ('nome', 'data_nascimento', 'telefone', 'endereco')  # Colunas visíveis na lista
    search_fields = ('nome', 'telefone')  # Campos para busca
    list_filter = ('data_nascimento',)  # Filtro por data de nascimento
    ordering = ('nome',)  # Ordem padrão por nome
