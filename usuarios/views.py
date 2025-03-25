# usuarios/views.py
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, PasswordResetConfirmView
from django.views import generic
from agendamentos.models import Agendamento
from pacientes.models import Paciente
from profissionais.models import Profissional
from django.utils.timezone import now
from django.db.models import Count
from django.contrib import messages
from django.contrib.auth.tokens import default_token_generator
from django.db.models.functions import ExtractMonth
from django.contrib.auth.mixins import LoginRequiredMixin
import logging
from django.http import HttpResponse
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from usuarios.forms import CustomUserCreationForm
from django.core.mail import send_mail
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate, login

logger = logging.getLogger(__name__)

# =========================
# VIEWS FORM-BASED (HTML)
# =========================

class CustomLoginView(LoginView):
    template_name = 'usuarios/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('agendamentos:listar_agendamentos')

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "home/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        agendamentos_por_mes = (
            Agendamento.objects.filter(data_inicio__year=now().year)
            .annotate(mes=ExtractMonth('data_inicio'))
            .values('mes')
            .annotate(total=Count('id'))
            .order_by('mes')
        )
        meses = [
            "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
            "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
        ]
        agendamentos_formatados = [
            {"mes": meses[item['mes'] - 1], "total": item['total']}
            for item in agendamentos_por_mes
        ]

        logger.debug("Dados para o gráfico: %s", agendamentos_formatados)

        context['total_agendamentos'] = Agendamento.objects.count()
        context['total_pacientes'] = Paciente.objects.count()
        context['total_profissionais'] = Profissional.objects.count()
        context['proximos_agendamentos'] = (
            Agendamento.objects.filter(data_inicio__gte=now())
            .order_by('data_inicio')[:5]
        )
        context['agendamentos_por_mes'] = agendamentos_formatados
        return context

class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('usuarios:login')
    template_name = 'usuarios/signup.html'

    def form_valid(self, form):
        user = form.save()
        messages.success(self.request, "Cadastro realizado com sucesso! Faça login para continuar.")
        return super().form_valid(form)

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'usuarios/password_reset_confirm.html'
    success_url = reverse_lazy('usuarios:password_reset_complete')

    def get(self, request, *args, **kwargs):
        uidb64 = kwargs.get('uidb64')
        token = kwargs.get('token')
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = User.objects.get(pk=uid)
            if default_token_generator.check_token(user, token):
                logger.info(f"✅ Token válido para o usuário {user.email}")
                return super().get(request, *args, **kwargs)
            else:
                logger.warning(f"❌ Token inválido para o usuário {user.email}")
                return HttpResponse("O link de redefinição de senha é inválido ou expirou.", status=400)
        except (ObjectDoesNotExist, ValueError, TypeError, UnicodeDecodeError):
            logger.error(f"❌ Erro ao decodificar UID ou usuário inexistente: {uidb64}")
            return HttpResponse("O link de redefinição de senha é inválido.", status=400)