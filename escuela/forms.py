from django import forms
from .models import Escuela

class EscuelaForm(forms.ModelForm):

    class Meta:
        model = Escuela

        fields=[
            'nombre_corto',
            'nombre_largo',
        ]

        labels={
            'nombre_corto':'Nombre Corto',
            'nombre_largo':'Nombre Largo',
        }


        widgets={
            'nombre_corto': forms.TextInput(attrs={'class':'form-control','id':'nom_corto', 'placeholder': 'Ingrese el nombre corto de la escuela'}),
            'nombre_largo': forms.TextInput(attrs={'class':'form-control','id':'nom_largo', 'placeholder': 'Ingrese el nombre completo de la escuela'}),
        }



