#salas/models.py

from django.db import models

class Sala(models.Model):
    numero = models.CharField(
        max_length=10,
        unique=True,
        verbose_name="Número da Sala",
        help_text="Identificação única da sala."
    )
    capacidade = models.PositiveIntegerField(
        verbose_name="Capacidade",
        help_text="Capacidade máxima da sala."
    )
    descricao = models.TextField(
        verbose_name="Descrição",
        blank=True,
        null=True,
        help_text="Descrição opcional da sala."
    )

    class Meta:
        verbose_name = "Sala"
        verbose_name_plural = "Salas"
        ordering = ['numero']

    def __str__(self):
        return f"Sala {self.numero}"
