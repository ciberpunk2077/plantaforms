from django.urls import path
from .views.planta import (
    PlantaCreateView, 
    PlantaListView, 
    PlantaDetailView,
    PlantaUpdateView,
    PlantaDeleteView, load_especies,
)
from .views.muestra import MuestraListView

app_name = 'catalogo'

urlpatterns = [
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