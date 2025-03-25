#cadastros/apps.py

from django.apps import AppConfig


class CadastrosConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "cadastros"
    verbose_name = "Gerenciamento de Cadastros"  # Nome amigável para o admin

