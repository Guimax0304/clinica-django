#agendamentos/models.py

from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from pacientes.models import Paciente
from profissionais.models import Profissional
from procedimentos.models import Procedimento
from salas.models import Sala
from datetime import timedelta

class Agendamento(models.Model):
    paciente = models.ForeignKey(
        Paciente, on_delete=models.CASCADE, related_name='agendamentos', verbose_name="Paciente"
    )
    profissional = models.ForeignKey(
        Profissional, on_delete=models.CASCADE, related_name='agendamentos', verbose_name="Profissional"
    )
    procedimento = models.ForeignKey(
        Procedimento, on_delete=models.CASCADE, null=True, blank=True, related_name='agendamentos', verbose_name="Procedimento"
    )
    sala = models.ForeignKey(
        Sala, on_delete=models.CASCADE, related_name='agendamentos', null=True, blank=True, verbose_name="Sala"
    )
    data_inicio = models.DateTimeField(verbose_name="Data de Início")
    data_fim = models.DateTimeField(blank=True, null=True, verbose_name="Data de Término")
    descricao = models.TextField(blank=True, default='', verbose_name="Descrição")
    cor = models.CharField(max_length=7, default='#3788d8', verbose_name="Cor do Evento")

    def clean(self):
        # Validação: Data de início não pode ser no passado
        if self.data_inicio and self.data_inicio < timezone.now() + timedelta(minutes=1):
            raise ValidationError("A data de início não pode ser no passado ou muito próxima ao horário atual.")

        # Validação: Data de término deve ser posterior à data de início
        if self.data_fim and self.data_inicio and self.data_inicio >= self.data_fim:
            raise ValidationError("A data de término deve ser posterior à data de início.")

        # Validação: Conflito de horários na sala
        if self.sala and self.data_inicio and self.data_fim:
            conflitos = Agendamento.objects.filter(
                sala=self.sala,
                data_inicio__lt=self.data_fim,
                data_fim__gt=self.data_inicio
            ).exclude(id=self.id)
            if conflitos.exists():
                raise ValidationError(f"A Sala {self.sala.numero} já está reservada nesse horário.")

    def __str__(self):
        return f"Agendamento de {self.paciente} com {self.profissional} em {self.data_inicio.strftime('%d/%m/%Y %H:%M')}"

    class Meta:
        ordering = ['-data_inicio']
        verbose_name = "Agendamento"
        verbose_name_plural = "Agendamentos"
