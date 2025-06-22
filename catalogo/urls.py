from django.urls import path
from .views.planta import (
    PlantaCreateView, 
    PlantaListView, 
    PlantaDetailView,
    PlantaUpdateView,
    PlantaDeleteView, load_especies,)
from .views.alga import *
from .views.muestra import MuestraListView

app_name = 'catalogo'

urlpatterns = [

    # URLs para algas
    path('algas/', AlgaListView.as_view(), name='alga-list'),
    path('algas/nueva/', AlgaCreateView.as_view(), name='alga-create'),
    path('algas/<int:pk>/', AlgaDetailView.as_view(), name='alga-detail'),
    path('algas/<int:pk>/editar/', AlgaUpdateView.as_view(), name='alga-update'),
    path('algas/<int:pk>/eliminar/', AlgaDeleteView.as_view(), name='alga-delete'),

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
    # ... otras URLs ...
]