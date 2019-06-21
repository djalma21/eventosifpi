from django.shortcuts import render, redirect, get_object_or_404
from .models import Inscricao, Evento, Submissao
from .forms import EventoForm, InscricaoForm, SubmissaoForm
from django.contrib.auth.decorators import login_required

def home(request):
    eventos = Evento.objects.all()
    return render(request,'home.html',{'eventos': eventos})

def listar_inscritos(request):
    inscritos = Inscricao.objects.all()
    return render(request,'listar_inscritos.html',{'inscritos': inscritos})

def listar_trabalhos(request):
    trabalhos = Submissao.objects.all()
    return render(request,'lista_de_trabalhos.html',{'trabalhos': trabalhos})
@login_required
def cadastrar_evento(request):
    form = EventoForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'cadastrar_evento.html', {'form': form})
@login_required
def submeter_trabalho(request):
    form = SubmissaoForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'Submeter_trabalho.html', {'form': form})
@login_required
def fazer_inscricao(request):
    form = InscricaoForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'fazer_inscricao.html', {'form': form})

def mostrar_evento(request, id):
    eventos = Evento.objects.filter(pk=id)
    return render(request, 'mostrar_evento.html', {'eventos': eventos})

def alterar_evento(request, id):
    evento = get_object_or_404(Evento, pk=id)
    form = EventoForm(request.POST or None, request.FILES or None, instance=evento)

    if form.is_valid():
        form.save()
        return redirect('home')

    return render(request, 'cadastrar_evento.html', {'form': form})

def alterar_inscricao(request, id):
    inscricao = get_object_or_404(Inscricao, pk=id)
    form = EventoForm(request.POST or None, request.FILES or None, instance=inscricao)

    if form.is_valid():
        form.save()
        return redirect('home')

    return render(request, 'fazer_inscricao.html', {'form': form})

def alterar_trabalho_submetido(request, id):
    trabalho = get_object_or_404(Submissao, pk=id)
    form = EventoForm(request.POST or None, request.FILES or None, instance=trabalho)

    if form.is_valid():
        form.save()
        return redirect('home')

    return render(request, 'submeter_trabalho.html', {'form': form})

def deletar_evento(request, id):
    eventos = get_object_or_404(Evento, pk=id)

    if request.method == 'POST':
        eventos.delete()
        return redirect('home')

    return render(request, 'deletar_evento.html', {'eventos': eventos})

def deletar_inscricao(request, id):
    inscricao = get_object_or_404(Inscricao, pk=id)

    if request.method == 'POST':
        inscricao.delete()
        return redirect('home')

    return render(request, 'deletar_inscricao.html', {'inscricao': inscricao})

def deletar_trabalho(request, id):
    trabalho = get_object_or_404(Submissao, pk=id)

    if request.method == 'POST':
        trabalho.delete()
        return redirect('home')

    return render(request, 'deletar_trabalho.html', {'trabalho': trabalho})