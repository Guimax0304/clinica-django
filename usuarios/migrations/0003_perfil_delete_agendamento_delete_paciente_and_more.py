# Generated by Django 4.2.16 on 2024-12-26 14:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("usuarios", "0002_agendamento"),
    ]

    operations = [
        migrations.CreateModel(
            name="Perfil",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "bio",
                    models.TextField(blank=True, null=True, verbose_name="Biografia"),
                ),
                (
                    "foto",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="perfil_fotos/",
                        verbose_name="Foto de Perfil",
                    ),
                ),
                (
                    "telefone",
                    models.CharField(
                        blank=True, max_length=15, null=True, verbose_name="Telefone"
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="perfil",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="Agendamento",
        ),
        migrations.DeleteModel(
            name="Paciente",
        ),
        migrations.DeleteModel(
            name="Procedimento",
        ),
        migrations.DeleteModel(
            name="Profissional",
        ),
    ]
