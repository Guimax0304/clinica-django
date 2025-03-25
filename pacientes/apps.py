#pacientes/apps.py

from django.apps import AppConfig


class PacientesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "pacientes"
    verbose_name = "Gerenciamento de Pacientes"  # Nome amigável para exibição no admin
