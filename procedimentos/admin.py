#procedimentos/admin.py

from django.contrib import admin
from .models import Procedimento

@admin.register(Procedimento)
class ProcedimentoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'preco')  # Mostra os campos na lista
    search_fields = ('nome', 'descricao')  # Adiciona barra de busca
    list_filter = ('preco',)  # Filtros por valores específicos
    ordering = ('nome',)  # Ordenação padrão
