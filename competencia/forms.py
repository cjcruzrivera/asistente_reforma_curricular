from django import forms
from .models import Competencia


class CompetenciaForm(forms.ModelForm):

    class Meta:
        model = Competencia

        fields = [
            'descripcion',
        ]
        labels = {
            'descripcion': 'Describa la competencia',
        }
        widgets = {
            'descripcion': forms.TextInput(attrs={'class': 'form-control', 'id': 'descripcion', 'placeholder': 'Competencia de aprendizaje'}),
        }

    def __init__(self, *args, **kwargs):
        super(CompetenciaForm, self).__init__(*args, **kwargs)
