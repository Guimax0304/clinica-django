#agendamentos/forms.py

from django import forms
from .models import Agendamento, Sala
from pacientes.models import Paciente
from profissionais.models import Profissional
from procedimentos.models import Procedimento
from django.utils import timezone

from django import forms
from .models import Agendamento
from django.utils.timezone import localtime

class AgendamentoForm(forms.ModelForm):
    class Meta:
        model = Agendamento
        fields = ['paciente', 'profissional', 'procedimento', 'sala', 'data_inicio', 'data_fim', 'descricao']
        widgets = {
            'data_inicio': forms.DateTimeInput(
                attrs={
                    'type': 'datetime-local',
                    'class': 'form-control',
                },
                format='%Y-%m-%dT%H:%M',  # Formato esperado pelo input datetime-local
            ),
            'data_fim': forms.DateTimeInput(
                attrs={
                    'type': 'datetime-local',
                    'class': 'form-control',
                },
                format='%Y-%m-%dT%H:%M',
            ),
            'descricao': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Adicione uma descrição (opcional)'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance:
            # Ajusta os valores iniciais para datetime-local
            self.fields['data_inicio'].initial = self.instance.data_inicio.strftime('%Y-%m-%dT%H:%M') if self.instance.data_inicio else None
            self.fields['data_fim'].initial = self.instance.data_fim.strftime('%Y-%m-%dT%H:%M') if self.instance.data_fim else None
        

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Ordenar os campos de seleção para melhorar a usabilidade
        self.fields['paciente'].queryset = Paciente.objects.order_by('nome')
        self.fields['profissional'].queryset = Profissional.objects.order_by('nome')
        self.fields['procedimento'].queryset = Procedimento.objects.order_by('nome')
        self.fields['sala'].queryset = Sala.objects.order_by('numero')

        # Definir placeholders adicionais e valores padrão
        self.fields['descricao'].help_text = "Descrição detalhada do agendamento (opcional)."
        self.fields['descricao'].required = False

    def clean(self):
        cleaned_data = super().clean()
        data_inicio = cleaned_data.get("data_inicio")
        data_fim = cleaned_data.get("data_fim")

        # Validar: data de início não pode ser no passado
        if data_inicio and data_inicio < timezone.now():
            self.add_error('data_inicio', "A data de início não pode ser no passado.")

        # Validar: data de término deve ser posterior à data de início
        if data_fim and data_fim <= data_inicio:
            self.add_error('data_fim', "A data de fim deve ser posterior à data de início.")

        return cleaned_data
