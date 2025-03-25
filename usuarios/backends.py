#usuaios/backends.py

from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
import logging

# Obtém o modelo de usuário configurado no projeto
UserModel = get_user_model()
logger = logging.getLogger(__name__)

#Backend de autenticação customizado que permite login usando o email.

class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserModel.objects.get(email=username)
            if user.check_password(password) and user.is_active:
                logger.info(f"Usuário autenticado com sucesso: {username}")
                return user
        except UserModel.DoesNotExist:
            logger.warning(f"Tentativa de login falhou para o e-mail: {username}")
        return None