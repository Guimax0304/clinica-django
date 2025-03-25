#profissionais/admin.py

from django.contrib import admin
from .models import Profissional

@admin.register(Profissional)
class ProfissionalAdmin(admin.ModelAdmin):
    list_display = ('nome', 'especialidade', 'telefone', 'email', 'data_contratacao')  # Campos exibidos na lista
    search_fields = ('nome', 'especialidade', 'email')  # Campos para a busca
    list_filter = ('especialidade', 'data_contratacao')  # Filtros laterais
    ordering = ('nome',)  # Ordenação padrão
    date_hierarchy = 'data_contratacao'  # Navegação por data
