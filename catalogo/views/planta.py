import logging
from django.urls import reverse_lazy
from django.contrib import messages
from ..forms.planta import PlantaForm
from django.http import HttpResponse
from django.template.loader import render_to_string
from ..models import Especie
from .muestra import MuestraCreateView, MuestraListView, MuestraDetailView, MuestraUpdateView, MuestraDeleteView

logger = logging.getLogger(__name__)


class PlantaCreateView(MuestraCreateView):
    """
    Vista especializada para crear muestras de tipo PLANTA
    """
    form_class = PlantaForm
    tipo_fijo = 'PLANTA'
    template_name = 'catalogo/planta_form.html'
    
    def get_form_kwargs(self):
        """Asegura que el tipo PLANTA se pase al formulario"""
        kwargs = super().get_form_kwargs()
        kwargs['tipo_muestra'] = self.tipo_fijo
        return kwargs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'titulo_pagina': "Nueva Planta",
            'es_planta': True,
            'subtitulo': "Complete los datos de la planta recolectada"
        })
        return context
    
    def get_success_url(self):
        return reverse_lazy('catalogo:planta-list')

    def form_valid(self, form):
        print("Datos del formulario:", form.cleaned_data)  # Ver qué datos llegan
        print("Archivo de imagen recibido:", form.files.get('imagen')) 
        form.instance.tipo_muestra = 'PLANTA'
        form.instance.uploaded_by = self.request.user  # Si tienes este campo
        
        if not form.cleaned_data.get('imagen'):
            form.add_error('imagen', 'Debe subir una imagen de la planta')
            return self.form_invalid(form)
            
        try:
            form.instance.tipo_muestra = 'PLANTA'
            self.object = form.save()  # Esto guardará la imagen automáticamente
            
            messages.success(
                self.request,
                f"Planta {self.object.nombre_cientifico} creada exitosamente!"
            )
            return super().form_valid(form)
            
        except Exception as e:
            logger.error(f"Error al guardar planta: {str(e)}", exc_info=True)
            messages.error(self.request, f"Error al guardar: {str(e)}")
            return self.form_invalid(form)


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


def load_especies(request):
    familia_id = request.GET.get('familia') or request.GET.get('familia_id')
    
    if not familia_id or familia_id == 'undefined':
        return HttpResponse('<option value="">---------</option>')
            
    try:
        especies = Especie.objects.filter(familia_id=int(familia_id)).order_by('nombre')
        options = ''.join(f'<option value="{e.id}">{e.nombre}</option>' for e in especies)
        return HttpResponse(options)
    except (ValueError, TypeError, Especie.DoesNotExist) as e:
        logger.error(f"Error cargando especies: {str(e)}")
        return HttpResponse('<option value="">Error cargando especies</option>')