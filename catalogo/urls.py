from django.urls import path
from .views.planta import PlantaListView, MuestraBiologicaPlantaCreateView
from .views.muestra import (
    MuestraListView, MuestraCreateView,
    MuestraUpdateView, MuestraDetailView,
    MuestraDeleteView,
)

app_name = 'catalogo'

urlpatterns = [
    # URLs generales para muestras
    path('muestras/', MuestraListView.as_view(), name='muestra-list'),
    path('muestras/nueva/', MuestraCreateView.as_view(), name='muestra-create'),
    path('muestras/<int:pk>/', MuestraDetailView.as_view(), name='muestra-detail'),
    path('muestras/<int:pk>/editar/', MuestraUpdateView.as_view(), name='muestra-update'),
    path('muestras/<int:pk>/eliminar/', MuestraDeleteView.as_view(), name='muestra-delete'),


        # ... Plantas ...
    path('plantas/', PlantaListView.as_view(), name='planta_list'),  # ✅ Correcto
    # path('plantas/add/', (MuestraBiologicaPlantaCreateView.as_view()), name="planta-add"),
    path('plantas/add/', MuestraBiologicaPlantaCreateView.as_view(), name="planta_create"),
    # path('plantas/<int:pk>/edit/', login_required(PlantaUpdateView.as_view()), name="planta-edit"),
    # path('plantas/<int:pk>/detail/', login_required(PlantaDetailView.as_view()), name="planta_detail"),


]