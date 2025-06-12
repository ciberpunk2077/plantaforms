from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from ..models import MuestraBiologica
from django.contrib.auth.mixins import PermissionRequiredMixin
from ..forms import muestra
from catalogo.forms.muestra import MuestraBiologicaForm 


class MuestraListView(ListView):
    model = MuestraBiologica
    template_name = 'catalogo/muestra_list.html'
    context_object_name = 'muestras'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        tipo = self.request.GET.get('tipo')
        if tipo:
            queryset = queryset.filter(tipo_muestra=tipo)
        return queryset.order_by('-fecha')

class MuestraCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'catalogo.add_muestrabiologica'
    model = MuestraBiologica
    form_class = MuestraBiologicaForm
    template_name = 'catalogo/muestra_form.html'
    
    # Parámetro para fijar el tipo desde la URL
    tipo_fijo = None
    
    def get_success_url(self):
        return reverse_lazy('catalogo:muestra-list')
    
    def get_initial(self):
        initial = super().get_initial()
        if self.tipo_fijo:
            initial['tipo_muestra'] = self.tipo_fijo
        return initial
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        # Obtener el tipo de muestra de la URL si no está fijo
        if not self.tipo_fijo:
            kwargs['tipo_muestra'] = self.kwargs.get('tipo')
        return kwargs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tipo = self.tipo_fijo or self.kwargs.get('tipo')
        context['titulo_pagina'] = f"Nueva Muestra de {tipo.capitalize()}"
        return context

class MuestraUpdateView(UpdateView):
    model = MuestraBiologica
    form_class = muestra
    template_name = 'catalogo/muestra_form.html'
    success_url = reverse_lazy('catalogo:muestra-list')

    def form_valid(self, form):
        messages.success(self.request, "Muestra actualizada exitosamente.")
        return super().form_valid(form)

class MuestraDetailView(DetailView):
    model = MuestraBiologica
    template_name = 'catalogo/muestra_detail.html'
    context_object_name = 'muestra'

class MuestraDeleteView(DeleteView):
    model = MuestraBiologica
    template_name = 'catalogo/muestra_confirm_delete.html'
    success_url = reverse_lazy('catalogo:muestra-list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Muestra eliminada exitosamente.")
        return super().delete(request, *args, **kwargs)
    


    