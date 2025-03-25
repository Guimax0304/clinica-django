#salas/forms.py

from django import forms
from .models import Sala

class SalaForm(forms.ModelForm):
    class Meta:
        model = Sala
        fields = ['numero', 'capacidade', 'descricao']
        widgets = {
            'numero': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o número da sala'
            }),
            'capacidade': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Capacidade da sala'
            }),
            'descricao': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Descrição da sala (opcional)',
                'rows': 3
            }),
        }
