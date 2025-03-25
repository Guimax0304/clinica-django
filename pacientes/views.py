#pacientes/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Paciente
from .forms import PacienteForm
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseNotAllowed
from datetime import date


# Função utilitária para serializar um objeto Paciente
def serialize_paciente(paciente):
    return {
        'id': paciente.id,
        'nome': paciente.nome,
        'telefone': paciente.telefone,
        'data_nascimento': paciente.data_nascimento,
        'endereco': paciente.endereco,
    }


# View para listar pacientes (HTML)
@login_required(login_url='usuarios:login')
def listar_pacientes(request):
    pacientes = Paciente.objects.all()
    return render(request, 'pacientes/listar.html', {'pacientes': pacientes})


# API: Listar pacientes (JSON)
@login_required(login_url='usuarios:login')
def api_listar_pacientes(request):
    pacientes = Paciente.objects.all()
    return JsonResponse({'pacientes': [serialize_paciente(p) for p in pacientes]})


# View para criar paciente (HTML)
@login_required(login_url='usuarios:login')
def criar_paciente(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Paciente criado com sucesso!")
            return redirect('pacientes:listar_pacientes')
        else:
            messages.error(request, "Erro ao criar paciente. Verifique os campos.")
    else:
        form = PacienteForm()
    return render(request, 'pacientes/criar.html', {'form': form})


# API: Criar paciente (JSON)
@login_required(login_url='usuarios:login')
def api_criar_paciente(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            paciente = form.save()
            return JsonResponse({'status': 'success', 'message': 'Paciente criado com sucesso.', 'paciente': serialize_paciente(paciente)})
        return JsonResponse({'status': 'error', 'errors': form.errors})
    return HttpResponseNotAllowed(['POST'])


# View para editar paciente (HTML)
@login_required(login_url='usuarios:login')
def editar_paciente(request, id):
    paciente = get_object_or_404(Paciente, id=id)
    if request.method == 'POST':
        # Carregar os dados do formulário enviado pelo usuário
        form = PacienteForm(request.POST, instance=paciente)
        if form.is_valid():
            form.save()  # Salvar as alterações no banco
            messages.success(request, "Paciente atualizado com sucesso!")
            return redirect('pacientes:listar_pacientes')
        else:
            messages.error(request, "Erro ao atualizar paciente. Verifique os campos.")
    else:
        # Carregar o formulário com os dados existentes do paciente
        form = PacienteForm(instance=paciente)
    
    return render(request, 'pacientes/editar.html', {'form': form, 'paciente': paciente})


# API: Editar paciente (JSON)
@login_required(login_url='usuarios:login')
def api_editar_paciente(request, id):
    try:
        paciente = Paciente.objects.get(id=id)
    except Paciente.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Paciente não encontrado.'})
    if request.method == 'POST':
        form = PacienteForm(request.POST, instance=paciente)
        if form.is_valid():
            paciente = form.save()
            return JsonResponse({'status': 'success', 'message': 'Paciente atualizado com sucesso.', 'paciente': serialize_paciente(paciente)})
        return JsonResponse({'status': 'error', 'errors': form.errors})
    return HttpResponseNotAllowed(['POST'])


# View para deletar paciente (HTML)
@login_required(login_url='usuarios:login')
def deletar_paciente(request, id):
    paciente = get_object_or_404(Paciente, id=id)
    
    if request.method == 'POST':  # Somente processar exclusão no método POST
        paciente.delete()
        messages.success(request, "Paciente deletado com sucesso!")
        return redirect('pacientes:listar_pacientes')

    # Renderizar a página de confirmação de exclusão
    return render(request, 'pacientes/deletar.html', {'paciente': paciente})


# API: Deletar paciente (JSON)
@login_required(login_url='usuarios:login')
def api_deletar_paciente(request, id):
    try:
        paciente = Paciente.objects.get(id=id)
    except Paciente.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Paciente não encontrado.'})
    if request.method == 'POST':
        paciente.delete()
        return JsonResponse({'status': 'success', 'message': 'Paciente deletado com sucesso.'})
    return HttpResponseNotAllowed(['POST'])
