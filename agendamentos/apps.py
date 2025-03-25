#agendamento/apps.py

from django.apps import AppConfig

class AgendamentosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'agendamentos'
    verbose_name = 'Gerenciamento de Agendamentos'

    def ready(self):
        # Importação de signals caso necessário no futuro
        # from . import signals
        pass
