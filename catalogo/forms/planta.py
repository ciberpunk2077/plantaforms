from django import forms
from ..models import MuestraBiologica,Especie, Familia
from .muestra import MuestraBiologicaForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit

class PlantaForm(MuestraBiologicaForm):
    familia = forms.ModelChoiceField(
        queryset=Familia.objects.all(),
        label="Familia",
        required=True,
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    
    class Meta(MuestraBiologicaForm.Meta):
        fields = [
            'tipo_muestra', 'nombre_cientifico', 'nombre_comun', 'familia', 'especie',
            'genero', 'fecha', 'numero_recolecta', 'municipio', 'colonia', 'localidad',
            'descripcion', 'nombre_colector', 'imagen', 'latitud', 'longitud'
        ]
        widgets = {
            'nombre_cientifico': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ej: Ej: Rosa rubiginosa'}),
            'nombre_comun': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ej: Rosa mosqueta'}),
            'numero_recolecta': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ej: INV-123'}),
            'colonia': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ej: san jose'}),
            'localidad': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ej: villahermosa'}),
            'municipio': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ej: centro'}),
            'nombre_colector': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ej: El PEPE'}),
            'latitud': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ej: 17.98996809279243'}),
            'longitud': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ej: -92.97312461534396'}),

            'fecha': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'tipo_muestra': forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        tipo_muestra = kwargs.pop('tipo_muestra', None)
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'campo1',
            'campo2',
            Submit('submit', 'Guardar', css_class='btn btn-primary')
        )
        # Especializaciones para plantas
        self.fields['nombre_comun'].required = True
        
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