from django.views.generic import ListView
from ..models import MuestraBiologica

class PlantaListView(ListView):
    model = MuestraBiologica
    template_name = 'catalogo/planta_list.html'
    context_object_name = 'plantas'

    def get_queryset(self):
        return super().get_queryset().filter(tipo_muestra='PLANTA')