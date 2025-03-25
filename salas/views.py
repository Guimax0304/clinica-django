from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Sala
from .forms import SalaForm

@login_required(login_url='usuarios:login')
def listar_salas(request):
    salas = Sala.objects.all()
    return render(request, 'salas/listar.html', {'salas': salas})

@login_required(login_url='usuarios:login')
def criar_sala(request):
    if request.method == 'POST':
        form = SalaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Sala criada com sucesso!")
            return redirect('salas:listar_salas')
    else:
        form = SalaForm()
    return render(request, 'salas/criar.html', {'form': form})

@login_required(login_url='usuarios:login')
def editar_sala(request, id):
    sala = get_object_or_404(Sala, id=id)
    if request.method == 'POST':
        form = SalaForm(request.POST, instance=sala)
        if form.is_valid():
            form.save()
            messages.success(request, "Sala atualizada com sucesso!")
            return redirect('salas:listar_salas')
    else:
        form = SalaForm(instance=sala)
    return render(request, 'salas/editar.html', {'form': form, 'sala': sala})

@login_required(login_url='usuarios:login')
def deletar_sala(request, id):
    sala = get_object_or_404(Sala, id=id)
    if request.method == 'POST':
        sala.delete()
        messages.success(request, "Sala deletada com sucesso!")
        return redirect('salas:listar_salas')
    return render(request, 'salas/deletar.html', {'sala': sala})
