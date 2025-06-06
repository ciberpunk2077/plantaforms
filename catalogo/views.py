from django.shortcuts import render
from .models import MuestraBiologica

def catalogo(request):
    muestras = MuestraBiologica.objects.all()
    return render(request, 'catalogo/catalogo.html', {'muestras': muestras})

def lista_plantas(request):
    plantas = MuestraBiologica.objects.filter(tipo_muestra='PLANTA')
    return render(request, 'catalogo/lista_plantas.html', {'plantas': plantas})

def home(request):
    return render(request, 'mi_app/home.html')