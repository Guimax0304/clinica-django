#procedimentos/apps.py

from django.apps import AppConfig

class ProcedimentosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'procedimentos'
    verbose_name = 'Gerenciamento de Procedimentos'
