#procedimentos/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Procedimento
from .forms import ProcedimentoForm

# Listar Procedimentos
@login_required(login_url='usuarios:login')
def listar_procedimentos(request):
    print("Usando o template de listar procedimentos")
    procedimentos = Procedimento.objects.all()
    return render(request, 'procedimentos/listar.html', {'procedimentos': procedimentos})

# Criar Procedimento
@login_required(login_url='usuarios:login')
def criar_procedimento(request):
    if request.method == 'POST':
        form = ProcedimentoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Procedimento criado com sucesso!")
            return redirect('procedimentos:listar_procedimentos')
        else:
            messages.error(request, "Erro ao criar procedimento. Verifique os campos.")
    else:
        form = ProcedimentoForm()
    return render(request, 'procedimentos/criar.html', {'form': form})

# Editar Procedimento
@login_required(login_url='usuarios:login')
def editar_procedimento(request, id):
    procedimento = get_object_or_404(Procedimento, id=id)
    if request.method == 'POST':
        form = ProcedimentoForm(request.POST, instance=procedimento)
        if form.is_valid():
            form.save()
            messages.success(request, "Procedimento atualizado com sucesso!")
            return redirect('procedimentos:listar_procedimentos')
        else:
            messages.error(request, "Erro ao atualizar procedimento. Verifique os campos.")
    else:
        form = ProcedimentoForm(instance=procedimento)
    return render(request, 'procedimentos/editar.html', {'form': form, 'procedimento': procedimento})

# Deletar Procedimento
@login_required(login_url='usuarios:login')
def deletar_procedimento(request, id):
    procedimento = get_object_or_404(Procedimento, id=id)
    if request.method == 'POST':
        procedimento.delete()
        messages.success(request, "Procedimento deletado com sucesso!")
        return redirect('procedimentos:listar_procedimentos')
    return render(request, 'procedimentos/deletar.html', {'procedimento': procedimento})
