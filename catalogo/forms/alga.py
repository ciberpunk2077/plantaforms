from django import forms
from ..models import MuestraBiologica, Especie, Familia, Municipio
from .muestra import MuestraBiologicaForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit

class AlgaForm(MuestraBiologicaForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    # Campo imagen personalizado

        
        self.fields['imagen'].widget = forms.ClearableFileInput(attrs={
            'class': 'form-control',
            'accept': 'image/*',
            'id': 'id_imagen'
        })
        self.fields['imagen'].required = True
        
    

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
            'tipo_muestra', 'nombre_cientifico', 'familia', 'especie',
            'municipio',  'imagen', 
        ]
        widgets = {
            'tipo_muestra': forms.HiddenInput(),
            'imagen': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*',
            }),
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
            
            'municipio': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Ej: centro'}),
            
            

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
            
            'familia',
            'especie',
            
            'municipio',
            
            'imagen',
            'latitud',
            'longitud',
            Submit('submit', 'Guardar', css_class='btn btn-primary')
        )
        
        # Especializaciones para plantas
        
        
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

        # if not self.instance.pk or 'imagen' in self.changed_data:
        #     if not cleaned_data.get('imagen'):
        #         raise forms.ValidationError({'imagen': 'Debe subir una imagen de la planta'})
        
        if familia and especie and especie.familia != familia:
            raise forms.ValidationError(
                "La especie seleccionada no pertenece a la familia elegida."
            )
        
        return cleaned_data