#procedimentos/models.py

from django.db import models
from django.utils.translation import gettext_lazy as _

class Procedimento(models.Model):

    # Nome do procedimento
    nome = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Nome do Procedimento",
        help_text="Digite o nome do procedimento."
    ) 

    # Descrição do procedimento
    descricao = models.TextField(
        verbose_name="Descrição",
        help_text="Descrição detalhada do procedimento.",
        blank=True,
        null=True
    )  

    # Preço do procedimento
    preco = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Preço",
        help_text="Digite o preço do procedimento."
    )
    # Duração do procedimento
    duracao = models.DurationField(
        verbose_name="Duração Estimada",
        help_text="Informe a duração estimada (HH:MM:SS)."
    )  

    class Meta:
        verbose_name = _("Procedimento")
        verbose_name_plural = _("Procedimentos")
        ordering = ["nome"]  # Ordena os procedimentos pelo nome

    def __str__(self):
        return self.nome
