from django.urls import reverse_lazy
from django.contrib import messages
from ..forms.planta import PlantaForm
from .muestra import MuestraCreateView, MuestraListView, MuestraDetailView, MuestraUpdateView, MuestraDeleteView

class PlantaCreateView(MuestraCreateView):
    """
    Vista especializada para crear muestras de tipo PLANTA
    """
    form_class = PlantaForm
    permission_required = 'catalogo.add_muestrabiologica'
    tipo_fijo = 'PLANTA'
    template_name = 'catalogo/planta_form.html'
    success_url = reverse_lazy('catalogo:planta-list')
    
    def get_form_kwargs(self):
        """Asegura que el tipo PLANTA se pase al formulario"""
        kwargs = super().get_form_kwargs()
        kwargs['tipo_muestra'] = 'PLANTA'  # Forzar el tipo
        return kwargs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'titulo_pagina': "Nueva Planta",
            'es_planta': True,
            'subtitulo': "Complete los datos de la planta recolectada"
        })
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(
            self.request, 
            f"Planta {form.instance.nombre_cientifico} registrada exitosamente!"
        )
        return response

class PlantaListView(MuestraListView):
    """Listado específico para plantas"""
    template_name = 'catalogo/planta_list.html'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(tipo_muestra='PLANTA').select_related(
            'especie', 'especie__familia', 'municipio'
        )
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'titulo_pagina': "Listado de Plantas",
            'subtitulo': "Plantas registradas en el sistema"
        })
        return context

class PlantaDetailView(MuestraDetailView):
    """Detalle específico para plantas"""
    template_name = 'catalogo/planta_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        planta = self.get_object()
        context.update({
            'titulo_pagina': f"Detalle de {planta.nombre_cientifico}",
            'es_planta': True,
            'subtitulo': "Información detallada de la planta"
        })
        return context
    
# En catalogo/views/planta.py
class PlantaUpdateView(MuestraUpdateView):
    """Vista para editar plantas"""
    template_name = 'catalogo/planta_form.html'
    tipo_fijo = 'PLANTA'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo_pagina'] = f"Editar {self.object.nombre_cientifico}"
        return context

class PlantaDeleteView(MuestraDeleteView):
    """Vista para eliminar plantas"""
    success_url = reverse_lazy('catalogo:planta-list')
    
    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        messages.success(request, "Planta eliminada correctamente")
        return response