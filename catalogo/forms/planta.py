from django import forms
from catalogo.models import MuestraBiologica, Especie, Familia
from .base import BaseForm

class MuestraBiologicaForm(BaseForm):
    familia = forms.ModelChoiceField(
        queryset=Familia.objects.all(),
        label="Familia",
        required=True,
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    
    class Meta:
        model = MuestraBiologica
        fields = [
            'nombre_cientifico', 'nombre_comun', 'especie',
            'genero', 'fecha', 'numero_recolecta', 'municipio', 'colonia',
            'descripcion', 'nombre_colector', 'imagen', 'latitud', 'longitud'
        ]
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'tipo_muestra': forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Establecer familia inicial si ya hay una especie seleccionada
        if self.instance.pk and self.instance.especie:
            self.fields['familia'].initial = self.instance.especie.familia
        
        # Filtrado dinámico de especies
        self.fields['especie'].queryset = Especie.objects.none()
        
        if 'familia' in self.data:
            try:
                familia_id = int(self.data.get('familia'))
                self.fields['especie'].queryset = Especie.objects.filter(
                    familia_id=familia_id
                ).order_by('nombre')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk and self.instance.especie:
            self.fields['especie'].queryset = self.instance.especie.familia.especie_set.order_by('nombre')