from django.db.models import Q
from catalogo.models import MuestraBiologica
from django.shortcuts import render

def buscar_muestras(request):
    query = request.GET.get('q', '')
    tipo = request.GET.get('tipo')  # Filtro por tipo (alga, hongo, etc.)
    
    # Base query
    resultados = MuestraBiologica.objects.all()
    
    # Búsqueda full-text
    if query:
        resultados = resultados.filter(
            Q(nombre_cientifico__icontains=query) |
            Q(nombre_comun__icontains=query) |
            Q(familia__nombre__icontains=query) |
            Q(especie__nombre__icontains=query)
        )
    
    # Filtro por tipo (opcional)
    if tipo and tipo in dict(MuestraBiologica.TIPO_MUESTRA_CHOICES):
        resultados = resultados.filter(tipo_muestra=tipo)
    
    context = {
        'resultados': resultados,
        'query': query,
        'tipos_muestra': MuestraBiologica.TIPO_MUESTRA_CHOICES
    }
    return render(request, 'catalogo/buscar/resultados.html', context)