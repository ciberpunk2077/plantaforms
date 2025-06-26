from django import forms
from catalogo.models import MuestraBiologica

class BusquedaForm(forms.Form):
    q = forms.CharField(
        label="Término de búsqueda",
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Nombre, familia, especie...'})
    )
    tipo = forms.ChoiceField(
        label="Filtrar por tipo",
        choices=MuestraBiologica.TIPO_MUESTRA_CHOICES,
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )