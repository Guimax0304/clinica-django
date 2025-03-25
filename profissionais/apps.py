#profissionais/apps.py

from django.apps import AppConfig

class ProfissionaisConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "profissionais"
    verbose_name = "Gerenciamento de Profissionais"  # Nome amigável no Django Admin
