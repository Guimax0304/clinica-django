#pacientes/models.py

from django.db import models
from datetime import date

# Modelo para armazenar informações de pacientes 
from django.db import models

class Paciente(models.Model):
    nome = models.CharField(max_length=100, unique=True, null=False, verbose_name="Nome Completo")
    data_nascimento = models.DateField(null=True, blank=True, verbose_name="Data de Nascimento")  # Agora é opcional
    idade = models.PositiveIntegerField(null=True, blank=True, verbose_name="Idade")  # Campo armazenável
    telefone = models.CharField(max_length=15, null=True, blank=True, verbose_name="Telefone")
    endereco = models.TextField(null=True, blank=True, verbose_name="Endereço")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"
        ordering = ['nome']


# Calcula a idade com base na data de nascimento
    @property
    def idade(self):
        today = date.today()
        return today.year - self.data_nascimento.year - ((today.month, today.day) < (self.data_nascimento.month, self.data_nascimento.day))

    class Meta:
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"
        ordering = ['nome']

