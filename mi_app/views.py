from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'mi_app/home.html')

def presentacion(request):
    return render(request, 'mi_app/presentacion.html')

def datos(request):
    return render(request, 'mi_app/datos.html')