from django.shortcuts import render, redirect
from .forms import CriarCarteiraForm, AdicionarAtivoForm, UsuarioForm
from .models import Carteira, Acao, Usuario

def criar_carteira(request):
    if request.method == 'POST':
        form = CriarCarteiraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('visualizar_carteira')
    else:
        form = CriarCarteiraForm()
    return render(request, 'criar_carteira.html', {'form': form})

def adicionar_ativo(request):
    if request.method == 'POST':
        form = AdicionarAtivoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('visualizar_carteira')
    else:
        form = AdicionarAtivoForm()
    return render(request, 'adicionar_ativo.html', {'form': form})

def visualizar_carteira(request):
    carteiras = Carteira.objects.all()
    return render(request, 'visualizar_carteira.html', {'carteiras': carteiras})

def usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('usuario')
    else:
        form = UsuarioForm()        
    return render(request, 'usuario.html', {'form': form})