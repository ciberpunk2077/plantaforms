from django.views.generic import CreateView, UpdateView, ListView
from django.urls import reverse_lazy
from ..models import Familia, Especie
from catalogo.forms.familia import FamiliaForm, EspecieForm

class FamiliaCreateView(CreateView):
    model = Familia
    form_class = FamiliaForm
    template_name = 'catalogo/familia_form.html'
    success_url = reverse_lazy('catalogo:familia_list')

class FamiliaUpdateView(UpdateView):
    model = Familia
    form_class = FamiliaForm
    template_name = 'catalogo/familia_form.html'
    success_url = reverse_lazy('catalogo:familia_list')

class FamiliaListView(ListView):
    model = Familia
    template_name = 'catalogo/familia_list.html'
    context_object_name = 'familias'

class EspecieCreateView(CreateView):
    model = Especie
    form_class = EspecieForm
    template_name = 'catalogo/especie_form.html'
    success_url = reverse_lazy('catalogo:especie_list')

class EspecieUpdateView(UpdateView):
    model = Especie
    form_class = EspecieForm
    template_name = 'catalogo/especie_form.html'
    success_url = reverse_lazy('catalogo:especie_list')

class EspecieListView(ListView):
    model = Especie
    template_name = 'catalogo/especie_list.html'
    context_object_name = 'especies'