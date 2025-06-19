from django import forms
from ..models import MuestraBiologica, Especie, Familia, Municipio
from .muestra import MuestraBiologicaForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit

class PlantaForm(MuestraBiologicaForm):
    # Campo imagen personalizado
    imagen = forms.ImageField(
        label="Imagen de la planta",
        required=True,
        widget=forms.ClearableFileInput(attrs={
            'class': 'form-control',
            'accept': 'image/*',
            'id': 'id_imagen'
        }),
        error_messages={
            'required': 'Debe subir una imagen de la planta',
            'invalid_image': 'El archivo debe ser una imagen válida (JPEG, PNG, etc.)'
        }
    )

    # Campo familia (solo una definición)
    familia = forms.ModelChoiceField(
        queryset=Familia.objects.all().order_by('nombre'),
        label="Familia",
        required=True,
        widget=forms.Select(attrs={
            'class': 'form-select',
            'hx-get': '/catalogo/ajax/load-especies/',
            'hx-target': '#id_especie',
            'hx-trigger': 'change',
        })
    )

    especie = forms.ModelChoiceField(
        queryset=Especie.objects.none(),
        label="Especie",
        required=True,
        widget=forms.Select(attrs={
            'class': 'form-select',
            'id': 'id_especie',
        }),
        empty_label="Seleccione una especie"
    )

    municipio = forms.ModelChoiceField(
        queryset=Municipio.objects.all().order_by('nombre'),
        label="Municipio",
        required=True,
        widget=forms.Select(attrs={
            'class': 'form-select',
            'placeholder': 'Seleccione un municipio'
        }),
        empty_label="---------"
    )
    
    class Meta(MuestraBiologicaForm.Meta):
        fields = [
            'tipo_muestra', 'nombre_cientifico', 'nombre_comun', 'familia', 'especie',
            'genero', 'fecha', 'numero_recolecta', 'municipio', 'colonia', 'localidad',
            'descripcion', 'nombre_colector', 'imagen', 'latitud', 'longitud'
        ]
        widgets = {
            'latitud': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: 17.98996809279243',
                'step': 'any',
                'id': 'latitud'
            }),
            'longitud': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: -92.97312461534396',
                'step': 'any',
                'id': 'longitud'
            }),

            'nombre_cientifico': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Rosa rubiginosa'}),
            'nombre_comun': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Rosa mosqueta'}),
            'numero_recolecta': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: INV-123'}),
            'colonia': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: san jose'}),
            'localidad': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: villahermosa'}),
            'municipio': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Ej: centro'}),
            'nombre_colector': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: El PEPE'}),
            
            'fecha': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'tipo_muestra': forms.HiddenInput(),
            # No definimos 'imagen' aquí porque ya está definido arriba
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        tipo_muestra = kwargs.pop('tipo_muestra', None)
        super().__init__(*args, **kwargs)
        
        # Configuración de crispy forms
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'tipo_muestra',
            'nombre_cientifico',
            'nombre_comun',
            'familia',
            'especie',
            'genero',
            'fecha',
            'numero_recolecta',
            'municipio',
            'colonia',
            'localidad',
            'descripcion',
            'nombre_colector',
            'imagen',
            'latitud',
            'longitud',
            Submit('submit', 'Guardar', css_class='btn btn-primary')
        )
        
        # Especializaciones para plantas
        self.fields['nombre_comun'].required = True
        
        # Manejo seguro de familia y especie
        if 'familia' in self.data:
            try:
                familia_id = int(self.data.get('familia'))
                self.fields['especie'].queryset = Especie.objects.filter(
                    familia_id=familia_id
                ).order_by('nombre')
            except (ValueError, TypeError):
                pass
        # Si es una instancia existente (edición)
        elif self.instance.pk and self.instance.especie:
            self.fields['especie'].queryset = Especie.objects.filter(
                familia=self.instance.especie.familia
            )
            
        # Configurar HTMX para mantener la funcionalidad dinámica
        self.fields['familia'].widget.attrs.update({
            'hx-get': '/catalogo/ajax/load-especies/',
            'hx-target': '#id_especie',
            'hx-trigger': 'change',
            'hx-swap': 'innerHTML',
            'hx-vals': '{familia_id: this.value}'
        })

    def clean(self):
        cleaned_data = super().clean()
        familia = cleaned_data.get('familia')
        especie = cleaned_data.get('especie')
        
        if familia and especie and especie.familia != familia:
            raise forms.ValidationError(
                "La especie seleccionada no pertenece a la familia elegida."
            )
        
        return cleaned_data