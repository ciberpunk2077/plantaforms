from django.urls import path
from .views.planta import (
    PlantaCreateView, 
    PlantaListView, 
    PlantaDetailView,
    PlantaUpdateView,
    PlantaDeleteView, load_especies,)
from .views.alga import *
from .views.familia import (  # Cambia este import
    FamiliaCreateView, FamiliaUpdateView, FamiliaListView,
    EspecieCreateView, EspecieUpdateView, EspecieListView
)
from .views.muestra import MuestraListView

app_name = 'catalogo'

urlpatterns = [

    # URLs para Familia
    path('familia/', FamiliaListView.as_view(), name='familia_list'),
    path('familia/nueva/', FamiliaCreateView.as_view(), name='familia_create'),
    path('familia/editar/<int:pk>/', FamiliaUpdateView.as_view(), name='familia_update'),
    
    # URLs para Especie
    path('especie/', EspecieListView.as_view(), name='especie_list'),
    path('especie/nueva/', EspecieCreateView.as_view(), name='especie_create'),
    path('especie/editar/<int:pk>/', EspecieUpdateView.as_view(), name='especie_update'),

    # URLs para algas
    path('algas/', AlgaListView.as_view(), name='alga-list'),#muestran todas la algas
    path('algas/nueva/', AlgaCreateView.as_view(), name='alga-create'),#formulario de algas
    path('algas/<int:pk>/', AlgaDetailView.as_view(), name='alga-detail'),#muestra la alga a detalle
    path('algas/<int:pk>/editar/', AlgaUpdateView.as_view(), name='alga-update'),#actualiza la informacion
    path('algas/<int:pk>/eliminar/', AlgaDeleteView.as_view(), name='alga-delete'),#elimina el alga

    # URLs para plantas
    path('plantas/', PlantaListView.as_view(), name='planta-list'),
    path('plantas/nueva/', PlantaCreateView.as_view(), name='planta-create'),
    path('plantas/<int:pk>/', PlantaDetailView.as_view(), name='planta-detail'),
    path('plantas/<int:pk>/editar/', PlantaUpdateView.as_view(), name='planta-update'),
    path('plantas/<int:pk>/eliminar/', PlantaDeleteView.as_view(), name='planta-delete'),

    #URLs especie
    path('ajax/load-especies/', load_especies, name='ajax_load_especies'),
    
    # URLs generales para muestras (opcional mantenerlas)
    path('muestras/', MuestraListView.as_view(), name='muestra-list'),
    path('muestras/nueva/', MuestraCreateView.as_view(), name='muestra-create'),
    path('muestras/<int:pk>/', MuestraDetailView.as_view(), name='muestra-detail'),
    path('muestras/<int:pk>/editar/', MuestraUpdateView.as_view(), name='muestra-update'),
    path('muestras/<int:pk>/eliminar/', MuestraDeleteView.as_view(), name='muestra-delete'),
    # ... otras URLs ...
]