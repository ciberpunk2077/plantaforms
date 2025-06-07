from catalogo.models import MuestraBiologica
from django import forms

class MuestraBiologicaForm(forms.ModelForm):
    class Meta:
        model = MuestraBiologica
        fields = '__all__'
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
            'descripcion': forms.Textarea(attrs={'rows': 3}),
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['especie'].queryset = Especie.objects.none()
        
        if 'familia' in self.data:
            try:
                familia_id = int(self.data.get('familia'))
                self.fields['especie'].queryset = Especie.objects.filter(familia_id=familia_id).order_by('nombre')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk and self.instance.especie:
            self.fields['especie'].queryset = self.instance.especie.familia.especie_set.order_by('nombre')