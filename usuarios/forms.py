#usuarios/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from pacientes.models import Paciente
from profissionais.models import Profissional
from procedimentos.models import Procedimento
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

telefone_validator = RegexValidator(r'^\+?1?\d{9,15}$', _('Número de telefone inválido.'))

def add_form_control_class(fields):
    for field in fields.values():
        field.widget.attrs['class'] = 'form-control'

class PacienteForm(forms.ModelForm):
    telefone = forms.CharField(
        validators=[telefone_validator],
        widget=forms.TextInput(attrs={'placeholder': _('Telefone')})
    )

    class Meta:
        model = Paciente
        fields = ['nome', 'telefone', 'endereco']
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': _('Nome completo')}),
            'endereco': forms.Textarea(attrs={'placeholder': _('Endereço')}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_form_control_class(self.fields)

class ProfissionalForm(forms.ModelForm):
    telefone = forms.CharField(
        validators=[telefone_validator],
        widget=forms.TextInput(attrs={'placeholder': _('Telefone')})
    )

    class Meta:
        model = Profissional
        fields = ['nome', 'especialidade', 'telefone']
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': _('Nome completo')}),
            'especialidade': forms.TextInput(attrs={'placeholder': _('Especialidade')}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_form_control_class(self.fields)

class ProcedimentoForm(forms.ModelForm):
    class Meta:
        model = Procedimento
        fields = ['nome', 'descricao', 'preco']
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': _('Nome do procedimento')}),
            'descricao': forms.Textarea(attrs={'placeholder': _('Descrição')}),
            'preco': forms.NumberInput(attrs={'placeholder': _('Preço')}),
        }

    def clean_preco(self):
        preco = self.cleaned_data.get('preco')
        if preco <= 0:
            raise forms.ValidationError(_("O preço deve ser maior que zero."))
        return preco

# Formulário de criação de usuário personalizado
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu e-mail'})
    )
    username = forms.CharField(
        label=_("Usuário"),
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': _('Usuário')}),
    )
    password1 = forms.CharField(
        label=_("Senha"),
        widget=forms.PasswordInput(attrs={'placeholder': _('Senha')}),
        required=True,
    )
    password2 = forms.CharField(
        label=_("Confirmação de Senha"),
        widget=forms.PasswordInput(attrs={'placeholder': _('Confirme a senha')}),
        required=True,
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_email(self):
        """ Verifica se o e-mail já existe antes de salvar """
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este e-mail já está em uso.")
        return email

    def save(self, commit=True):
        """ Garante que o e-mail seja salvo corretamente """
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]  # Salva corretamente
        if commit:
            user.save()
        return user
