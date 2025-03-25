#profissionais/models.py

from django.db import models
from django.core.validators import RegexValidator

# Modelo para Profissional
class Profissional(models.Model):
    nome = models.CharField(
        max_length=100,
        unique=True,
        null=False,
        verbose_name="Nome Completo",
        help_text="Nome completo do profissional."
    )
    especialidade = models.CharField(
        max_length=100,
        verbose_name="Especialidade",
        help_text="Área de especialização do profissional."
    )
    telefone = models.CharField(
        max_length=15,
        validators=[RegexValidator(r'^\d{10,15}$', message="O telefone deve conter entre 10 a 15 dígitos.")],
        verbose_name="Telefone",
        help_text="Telefone do profissional, com DDD."
    )
    cpf = models.CharField(
        max_length=11,
        unique=True,
        null=True,
        blank=True,
        verbose_name="CPF",
        help_text="CPF do profissional (11 dígitos, apenas números).",
        validators=[RegexValidator(r'^\d{11}$', message="O CPF deve conter exatamente 11 dígitos.")]
    )
    email = models.EmailField(
        unique=True,
        null=True,
        blank=True,
        verbose_name="E-mail",
        help_text="E-mail de contato do profissional (opcional)."
    )
    data_contratacao = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data de Contratação",
        help_text="Data de início do vínculo com a instituição (opcional)."
    )

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Profissional"
        verbose_name_plural = "Profissionais"
        ordering = ['nome']  # Ordena os profissionais pelo nome
