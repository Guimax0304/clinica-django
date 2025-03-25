# agendamentos/views.py

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View, DetailView
from django.contrib import messages
from django.urls import reverse_lazy
from django.http import JsonResponse, HttpResponseBadRequest
from django.utils import timezone
from django.core.exceptions import ValidationError
from .models import Agendamento
from .forms import AgendamentoForm
from pacientes.models import Paciente
from profissionais.models import Profissional

# View para listar agendamentos
class ListarAgendamentosView(LoginRequiredMixin, ListView):
    """Lista todos os agendamentos futuros"""
    model = Agendamento
    template_name = 'agendamentos/listar_agendamentos.html'
    context_object_name = 'agendamentos'
    login_url = 'usuarios:login'

    def get_queryset(self):
        """Retorna apenas agendamentos futuros com dados otimizados."""
        return Agendamento.objects.filter(data_inicio__gte=timezone.now()).select_related(
            'paciente', 'profissional', 'procedimento', 'sala'
        )

    def get_context_data(self, **kwargs):
        """Adiciona pacientes e profissionais ao contexto."""
        context = super().get_context_data(**kwargs)
        context['pacientes'] = Paciente.objects.all()
        context['profissionais'] = Profissional.objects.all()
        return context

# View para criar um novo agendamento
class CriarAgendamentoView(LoginRequiredMixin, CreateView):
    """Criação de agendamento"""
    model = Agendamento
    form_class = AgendamentoForm
    template_name = 'agendamentos/criar_agendamento.html'
    success_url = reverse_lazy('agendamentos:listar_agendamentos')
    login_url = 'usuarios:login'

    def form_valid(self, form):
        """Valida e salva o agendamento"""
        agendamento = form.save(commit=False)
        try:
            agendamento.clean()  # Validações do model
            agendamento.save()
            messages.success(self.request, "Agendamento criado com sucesso!")
            return super().form_valid(form)
        except ValidationError as e:
            form.add_error(None, e.message)
            return self.form_invalid(form)

# View para editar um agendamento existente
class EditarAgendamentoView(LoginRequiredMixin, UpdateView):
    """Edição de agendamento existente"""
    model = Agendamento
    form_class = AgendamentoForm
    template_name = 'agendamentos/editar_agendamento.html'
    success_url = reverse_lazy('agendamentos:listar_agendamentos')
    login_url = 'usuarios:login'

    def form_valid(self, form):
        """Valida e salva as alterações no agendamento"""
        agendamento = form.save(commit=False)
        try:
            agendamento.clean()
            agendamento.save()
            messages.success(self.request, "Agendamento atualizado com sucesso!")
            return super().form_valid(form)
        except ValidationError as e:
            form.add_error(None, e.message)
            return self.form_invalid(form)

# View para deletar um agendamento
class DeletarAgendamentoView(LoginRequiredMixin, DeleteView):
    """Exclusão de agendamento"""
    model = Agendamento
    template_name = 'agendamentos/deletar_agendamento.html'
    success_url = reverse_lazy('agendamentos:listar_agendamentos')
    login_url = 'usuarios:login'

    def delete(self, request, *args, **kwargs):
        """Adiciona mensagem de sucesso após exclusão"""
        messages.success(self.request, "Agendamento deletado com sucesso!")
        return super().delete(request, *args, **kwargs)

# View para eventos em JSON
class EventosJsonView(LoginRequiredMixin, View):
    """Retorna eventos no formato JSON para o calendário"""
    login_url = 'usuarios:login'

    def get(self, request, *args, **kwargs):
        try:
            agendamentos = Agendamento.objects.select_related('paciente', 'profissional', 'procedimento')
            eventos = [
                {
                    'id': agendamento.pk,
                    'title': f"{agendamento.paciente.nome} - {agendamento.procedimento.nome if agendamento.procedimento else 'Sem Procedimento'}",
                    'start': agendamento.data_inicio.isoformat(),
                    'end': agendamento.data_fim.isoformat() if agendamento.data_fim else agendamento.data_inicio.isoformat(),
                    'color': agendamento.cor,
                }
                for agendamento in agendamentos
            ]
            return JsonResponse(eventos, safe=False)
        except Exception as e:
            return HttpResponseBadRequest(f"Erro ao carregar eventos: {str(e)}")

# View para detalhes do agendamento
class DetalhesAgendamentoView(DetailView):
    """Detalhes de um agendamento"""
    model = Agendamento
    template_name = 'agendamentos/detalhes_agendamento.html'
    context_object_name = 'agendamento'

# View para exclusão via AJAX
class ExcluirAgendamentoAjaxView(View):
    """Permite excluir agendamentos via requisições AJAX"""
    def delete(self, request, pk, *args, **kwargs):
        # Recupera o agendamento com base no ID fornecido
        agendamento = get_object_or_404(Agendamento, pk=pk)
        try:
            # Tenta excluir o agendamento
            agendamento.delete()
            # Retorna uma resposta JSON de sucesso
            return JsonResponse({'message': 'Agendamento excluído com sucesso!'}, status=200)
        except Exception as e:
            # Captura qualquer erro e retorna como resposta JSON
            return JsonResponse({'error': str(e)}, status=500)