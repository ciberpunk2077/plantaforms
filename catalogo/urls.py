from django.urls import path
from .views.planta import PlantaListView
from .views.muestra import (
    MuestraListView, MuestraCreateView,
    MuestraUpdateView, MuestraDetailView,
    MuestraDeleteView
)

app_name = 'catalogo'

urlpatterns = [
    path('muestras/', MuestraListView.as_view(), name='muestra-list'),
    path('muestras/nueva/', MuestraCreateView.as_view(), name='muestra-create'),
    path('muestras/<int:pk>/', MuestraDetailView.as_view(), name='muestra-detail'),
    path('muestras/<int:pk>/editar/', MuestraUpdateView.as_view(), name='muestra-update'),
    path('muestras/<int:pk>/eliminar/', MuestraDeleteView.as_view(), name='muestra-delete'),


        # ... Plantas ...
    path('plantas/', PlantaListView.as_view(), name='planta_list'),  # ✅ Correcto

]