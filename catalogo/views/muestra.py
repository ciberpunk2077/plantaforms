from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from ..models import MuestraBiologica
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

class MuestraCreateView(CreateView):
    model = MuestraBiologica
    form_class = muestra
    template_name = 'catalogo/muestra_form.html'
    success_url = reverse_lazy('catalogo:muestra-list')

    def form_valid(self, form):
        messages.success(self.request, "Muestra creada exitosamente.")
        return super().form_valid(form)

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