from django import forms
from .models import Paciente

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['nome', 'data_nascimento', 'telefone', 'endereco']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Adicionar classes CSS para estilizar os campos
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})