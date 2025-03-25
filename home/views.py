#home/views.py

from django.shortcuts import render
from django.http import JsonResponse
from django.utils.timezone import now
from django.db.models.functions import ExtractMonth
from django.db.models import Count

# Caso você utilize DRF para algo mais complexo
from rest_framework.response import Response
from rest_framework import viewsets

# Importe seus models reais
from agendamentos.models import Agendamento
from pacientes.models import Paciente
from profissionais.models import Profissional


def home(request):
    """
    View que renderiza o 'home.html' com dados
    para exibir na página (HTML + Chart.js).
    """
    # Resumos
    total_agendamentos = Agendamento.objects.count()
    total_pacientes = Paciente.objects.count()
    total_profissionais = Profissional.objects.count()

    # Próximos 5 agendamentos
    proximos_agendamentos = (
        Agendamento.objects
        .filter(data_inicio__gte=now())
        .order_by('data_inicio')[:5]
    )

    # Quantidade de agendamentos por mês
    agendamento_mes = (
        Agendamento.objects
        .annotate(mes=ExtractMonth('data_inicio'))
        .values('mes')
        .annotate(total=Count('id'))
        .order_by('mes')
    )

    # Mapeamento do número do mês -> nome do mês
    meses_nomes = {
        1: "Janeiro", 2: "Fevereiro", 3: "Março", 4: "Abril",
        5: "Maio", 6: "Junho", 7: "Julho", 8: "Agosto",
        9: "Setembro", 10: "Outubro", 11: "Novembro", 12: "Dezembro"
    }

    # Montar uma lista para o Chart.js
    agendamentos_por_mes = []
    for item in agendamento_mes:
        numero_mes = item['mes']
        agendamentos_por_mes.append({
            "mes": meses_nomes.get(numero_mes, "Indefinido"),
            "total": item['total']
        })

    # Exemplo de como você poderia acrescentar "2º dataset" (caso tenha algo do tipo “Retorno” ou outro campo).
    # Por hora, deixaremos só o "total". Se quiser multi-dataset, teria "total_consultas", "total_retornos", etc.

    # Montar o contexto para repassar ao template
    context = {
        'total_agendamentos': total_agendamentos,
        'total_pacientes': total_pacientes,
        'total_profissionais': total_profissionais,
        'proximos_agendamentos': proximos_agendamentos,
        'agendamentos_por_mes': agendamentos_por_mes,
    }
    return render(request, 'home/home.html', context)


def home_api(request):
    """
    Retorna os mesmos dados de 'home()', mas em formato JSON (para AJAX/Fetch).
    Opcional, mas útil se você quiser recarregar dados dinamicamente.
    """
    total_agendamentos = Agendamento.objects.count()
    total_pacientes = Paciente.objects.count()
    total_profissionais = Profissional.objects.count()

    proximos_agendamentos_qs = (
        Agendamento.objects
        .filter(data_inicio__gte=now())
        .order_by('data_inicio')[:5]
        .values('id', 'data_inicio', 'paciente__nome', 'profissional__nome')
    )
    proximos_agendamentos = [
        {
            "id": item["id"],
            "data_inicio": item["data_inicio"],
            "paciente": {"nome": item["paciente__nome"]},
            "profissional": {"nome": item["profissional__nome"]},
        }
        for item in proximos_agendamentos_qs
    ]

    agendamento_mes = (
        Agendamento.objects
        .annotate(mes=ExtractMonth('data_inicio'))
        .values('mes')
        .annotate(total=Count('id'))
        .order_by('mes')
    )

    meses_nomes = {
        1: "Janeiro", 2: "Fevereiro", 3: "Março", 4: "Abril",
        5: "Maio", 6: "Junho", 7: "Julho", 8: "Agosto",
        9: "Setembro", 10: "Outubro", 11: "Novembro", 12: "Dezembro"
    }

    agendamentos_por_mes = []
    for item in agendamento_mes:
        numero_mes = item['mes']
        agendamentos_por_mes.append({
            "mes": meses_nomes.get(numero_mes, "Indefinido"),
            "total": item['total']
        })

    data = {
        "total_agendamentos": total_agendamentos,
        "total_pacientes": total_pacientes,
        "total_profissionais": total_profissionais,
        "proximos_agendamentos": proximos_agendamentos,
        "agendamentos_por_mes": agendamentos_por_mes,
    }
    return JsonResponse(data)


class HomeViewSet(viewsets.ViewSet):
    """
    Exemplo de ViewSet se usar Django REST Framework c/ roteadores.
    Não é obrigatório se usar apenas as function-based views acima.
    """
    def list(self, request):
        total_agendamentos = Agendamento.objects.count()
        total_pacientes = Paciente.objects.count()
        total_profissionais = Profissional.objects.count()
        data = {
            "total_agendamentos": total_agendamentos,
            "total_pacientes": total_pacientes,
            "total_profissionais": total_profissionais,
        }
        return Response(data)
