# Generated by Django 4.2.16 on 2024-10-27 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("usuarios", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Agendamento",
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
                ("titulo", models.CharField(max_length=100)),
                ("data_inicio", models.DateTimeField()),
                ("data_fim", models.DateTimeField(blank=True, null=True)),
                ("cor", models.CharField(blank=True, max_length=7, null=True)),
            ],
        ),
    ]
