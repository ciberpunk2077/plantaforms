from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import PermissionRequiredMixin
from catalogo.models import MuestraBiologica
from catalogo.forms.planta import MuestraBiologicaForm

class PlantaListView(ListView):
    model = MuestraBiologica
    template_name = 'catalogo/planta_list.html'
    context_object_name = 'plantas'
    paginate_by = 20
    
    def get_queryset(self):
        return MuestraBiologica.objects.filter(tipo_muestra='PLANTA').order_by('-fecha')

class MuestraBiologicaPlantaCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'catalogo.add_muestrabiologica'  # Correcto según tu modelo
    model = MuestraBiologica  # Tu modelo principal
    form_class = MuestraBiologicaForm  # Asegúrate que este formulario existe
    template_name = 'catalogo/planta_form.html'
    success_url = reverse_lazy('catalogo:planta_list')
    
    def get_form_kwargs(self):
        """Inyecta el usuario actual al formulario"""
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
    
    def form_valid(self, form):
        """Lógica post-validación"""
        # Asignación automática de campos si es necesario
        if not form.instance.nombre_colector:
            form.instance.nombre_colector = self.request.user.get_full_name()
            
        response = super().form_valid(form)
        messages.success(self.request, 'Muestra de planta creada exitosamente')
        return response
    
    def get_context_data(self, **kwargs):
        """Agrega contexto adicional al template"""
        context = super().get_context_data(**kwargs)
        context['tipos_muestra'] = MuestraBiologica.TIPO_MUESTRA_CHOICES
        return context
    permission_required = 'catalogo.add_planta'
    model = MuestraBiologica
    form_class = MuestraBiologicaForm
    template_name = 'catalogo/planta_form.html'  # Asegúrate de crear este template
    success_url = reverse_lazy('catalogo:planta_list')  # Redirige al listado después de crear
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
    
    def form_valid(self, form):
        # Aquí puedes añadir lógica adicional antes de guardar
        response = super().form_valid(form)
        messages.success(self.request, 'Muestra creada exitosamente')
        return response