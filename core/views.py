from django.shortcuts import render, redirect
from .models import Inscricao, Evento
from .forms import EventoForm, InscricaoForm

# def home(request):
#     return render(request, "home.html")

def home(request):
    eventos = Evento.objects.all()
    return render(request,'home.html',{'eventos': eventos})

def listar_inscritos(request):
    inscritos = Inscricao.objects.all().order_by('evento')
    return render(request,'listar_inscritos.html',{'inscritos': inscritos})


def cadastrar_evento(request):
    form = EventoForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'cadastrar_evento.html', {'form': form})


def fazer_inscricao(request):
    form = InscricaoForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'fazer_inscricao.html', {'form': form})

def mostrar_evento(request, id):
    eventos = Evento.objects.filter(pk=id)
    return render(request, 'mostrar_evento.html', {'eventos': eventos})