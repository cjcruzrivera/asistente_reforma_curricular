from django import forms
from .models import Usuario

class UsuarioForm(forms.ModelForm):

    class Meta:
        model = Usuario

        fields=[
            'username',
            'nombre',
            'apellidos',
            'email',
            'password',
            'escuela',
            'roles'
        ]

        labels={
            'username':'Nombre Corto',
            'nombre':'Nombre',
            'apellidos':'Apellidos',
            'email':'Correo Electronico',
            'password': 'Password',
            'escuela':'Escuela',
            'roles': 'Roles'
        }


        widgets={
            'username': forms.TextInput(attrs={'class':'form-control','id':'nom_corto', 'placeholder': 'Ingrese el nombre corto de usuario'}),
            'nombre': forms.TextInput(attrs={'class':'form-control','id':'nombre', 'placeholder': 'Ingrese el nombre del usuario'}),
            'apellidos': forms.TextInput(attrs={'class':'form-control','id':'apellidos', 'placeholder': 'Ingrese los apellidos del usuario'}),
            'email': forms.EmailInput(attrs={'class':'form-control','id':'email', 'placeholder': 'Ingrese el correo electronico'}),
            'password': forms.PasswordInput(attrs={'class':'form-control','id':'password'}),
            'escuela': forms.Select(attrs={'class':'form-control','id':'escuela'}),
            'roles': forms.CheckboxSelectMultiple(),
        }



