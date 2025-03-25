#cadastros/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Cadastro
from .forms import CadastroForm

@login_required
def cadastros_view(request):
    """
    Página principal de cadastros.
    """
    return render(request, 'cadastros/cadastros.html')

@login_required
def criar_cadastro(request):
    """
    View para criar um novo cadastro.
    """
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Cadastro criado com sucesso!")
            return redirect('cadastros:listar_cadastros')
        else:
            messages.error(request, "Erro ao criar o cadastro. Verifique os dados informados.")
    else:
        form = CadastroForm()

    return render(request, 'cadastros/criar_cadastro.html', {'form': form})

@login_required
def listar_cadastros(request):
    """
    View para listar cadastros existentes.
    """
    cadastros = Cadastro.objects.all().order_by('-criado_em')
    return render(request, 'cadastros/listar_cadastros.html', {'cadastros': cadastros})

@login_required
def editar_cadastro(request, pk):
    """
    View para editar um cadastro existente.
    """
    cadastro = get_object_or_404(Cadastro, pk=pk)
    if request.method == 'POST':
        form = CadastroForm(request.POST, instance=cadastro)
        if form.is_valid():
            form.save()
            messages.success(request, "Cadastro atualizado com sucesso!")
            return redirect('cadastros:listar_cadastros')
        else:
            messages.error(request, "Erro ao atualizar o cadastro. Verifique os dados informados.")
    else:
        form = CadastroForm(instance=cadastro)

    return render(request, 'cadastros/editar_cadastro.html', {'form': form})

@login_required
def deletar_cadastro(request, pk):
    """
    View para excluir um cadastro existente.
    """
    cadastro = get_object_or_404(Cadastro, pk=pk)
    if request.method == 'POST':
        cadastro.delete()
        messages.success(request, "Cadastro excluído com sucesso!")
        return redirect('cadastros:listar_cadastros')

    return render(request, 'cadastros/deletar_cadastro.html', {'cadastro': cadastro})
