# Generated by Django 4.2.16 on 2025-01-01 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Procedimento",
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
                    "nome",
                    models.CharField(
                        help_text="Digite o nome do procedimento.",
                        max_length=100,
                        unique=True,
                        verbose_name="Nome do Procedimento",
                    ),
                ),
                (
                    "descricao",
                    models.TextField(
                        blank=True,
                        help_text="Descrição detalhada do procedimento.",
                        null=True,
                        verbose_name="Descrição",
                    ),
                ),
                (
                    "preco",
                    models.DecimalField(
                        decimal_places=2,
                        help_text="Digite o preço do procedimento.",
                        max_digits=10,
                        verbose_name="Preço",
                    ),
                ),
                (
                    "duracao",
                    models.DurationField(
                        help_text="Informe a duração estimada (HH:MM:SS).",
                        verbose_name="Duração Estimada",
                    ),
                ),
            ],
            options={
                "verbose_name": "Procedimento",
                "verbose_name_plural": "Procedimentos",
                "ordering": ["nome"],
            },
        ),
    ]
