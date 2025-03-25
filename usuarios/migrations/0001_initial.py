# Generated by Django 4.2.16 on 2024-10-12 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Paciente",
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
                ("nome", models.CharField(max_length=100, unique=True)),
                ("data_nascimento", models.DateField()),
                ("idade", models.IntegerField()),
                ("telefone", models.CharField(max_length=15)),
                ("endereco", models.TextField()),
            ],
        ),
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
                ("nome", models.CharField(max_length=100, unique=True)),
                ("descricao", models.TextField()),
                ("preco", models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name="Profissional",
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
                ("nome", models.CharField(max_length=100, unique=True)),
                ("especialidade", models.CharField(max_length=100)),
                ("telefone", models.CharField(max_length=15)),
            ],
        ),
    ]
