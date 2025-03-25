#profissionais/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Profissional
from .forms import ProfissionalForm
from django.contrib import messages  # Para mensagens de feedback ao usuário


# Lista todos os profissionais cadastrados.
@login_required(login_url='usuarios:login')
def listar_profissionais(request):
    profissionais = Profissional.objects.all().order_by('nome')  # Ordena por nome
    return render(request, 'profissionais/listar.html', {'profissionais': profissionais})


# Cria um novo profissional.
@login_required(login_url='usuarios:login')
def criar_profissional(request):
    if request.method == 'POST':
        form = ProfissionalForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profissional criado com sucesso.')
            return redirect('profissionais:listar_profissionais')
        else:
            messages.error(request, 'Erro ao criar profissional. Verifique os dados informados.')
    else:
        form = ProfissionalForm()
    return render(request, 'profissionais/criar.html', {'form': form})


# Edita os dados de um profissional existente.
@login_required(login_url='usuarios:login')
def editar_profissional(request, id):
    profissional = get_object_or_404(Profissional, id=id)

    if request.method == 'POST':
        form = ProfissionalForm(request.POST, instance=profissional)
        if form.is_valid():
            form.save()
            messages.success(request, "Profissional atualizado com sucesso!")
            return redirect('profissionais:listar_profissionais')
        else:
            messages.error(request, "Erro ao atualizar profissional. Verifique os campos.")
    else:
        # Força o carregamento correto da data no formato esperado pelo HTML5
        initial_data = {'data_contratacao': profissional.data_contratacao.strftime('%Y-%m-%d') if profissional.data_contratacao else ''}
        form = ProfissionalForm(instance=profissional, initial=initial_data)

    return render(request, 'profissionais/editar.html', {'form': form, 'profissional': profissional})




# Deleta um profissional após confirmação.
@login_required(login_url='usuarios:login')
def deletar_profissional(request, id):
    profissional = get_object_or_404(Profissional, id=id)  # Corrigido uso da variável
    if request.method == 'POST':
        profissional.delete()
        messages.success(request, 'Profissional deletado com sucesso.')
        return redirect('profissionais:listar_profissionais')
    return render(request, 'profissionais/deletar.html', {'profissional': profissional})
