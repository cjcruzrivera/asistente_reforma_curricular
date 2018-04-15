from django import forms
from usuario.models import Usuario

class UsuarioForm(forms.ModelForm):

    class Meta:

        fields=[
            'nombre',
        ]