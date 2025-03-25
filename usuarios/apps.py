# usuarios/apps.py

from django.apps import AppConfig
import logging


logger = logging.getLogger(__name__)


class UsuariosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'usuarios'

    def ready(self):
        try:
            import usuarios.signals
            logger.info("Aplicativo 'usuarios' inicializado com sucesso.")
        except ImportError as e:
            logger.error(f"Erro ao importar sinais: {e}")