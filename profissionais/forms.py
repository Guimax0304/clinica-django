#profissionais/forms.py

from django import forms
from .models import Profissional
from validate_docbr import CPF

class ProfissionalForm(forms.ModelForm):
    class Meta:
        model = Profissional
        fields = ['nome', 'especialidade', 'telefone', 'cpf', 'email', 'data_contratacao']
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o nome completo'
            }),
            'especialidade': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Informe a especialidade'
            }),
            'telefone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o telefone (somente números)'
            }),
            'cpf': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o CPF (somente números)'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o e-mail'
            }),
            'data_contratacao': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
                'placeholder': 'Selecione a data de contratação'
            }),
        }

    def clean_data_contratacao(self):
        data = self.cleaned_data.get('data_contratacao')
        if not data:
            raise forms.ValidationError("A data de contratação é obrigatória.")
        return data

    def clean_telefone(self):
        telefone = self.cleaned_data.get('telefone')
        if telefone and (not telefone.isdigit() or not (10 <= len(telefone) <= 15)):
            raise forms.ValidationError("O telefone deve conter entre 10 e 15 dígitos.")
        return telefone

    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf')
        validador = CPF()
        if not cpf or not validador.validate(cpf):
            raise forms.ValidationError("Por favor, insira um CPF válido.")
        return cpf
