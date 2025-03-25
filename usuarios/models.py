#usuarios/models.py

from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from PIL import Image


#Modelo de perfil para armazenar informações adicionais de um usuário.
# Relacionado ao modelo de usuário através de um OneToOneField.
class Perfil(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='perfil')
    bio = models.TextField(blank=True, null=True, verbose_name="Biografia")
    foto = models.ImageField(upload_to='perfil_fotos/', blank=True, null=True, verbose_name="Foto de Perfil")
    telefone = models.CharField(max_length=15, blank=True, null=True, verbose_name="Telefone")
    validators=[RegexValidator(r'^\+?1?\d{9,15}$', _('Número de telefone inválido'))]

    def __str__(self):
        return f"Perfil de {self.user.username}"
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.foto:
            img = Image.open(self.foto.path)
            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(self.foto.path) 
