from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from .models import Usuario

class UsuarioCreateForm(UserCreationForm):

    class Meta:
        model = Usuario

        fields=[
            'username',
            'first_name',
            'last_name',
            'email',
            'escuela',
            'rol'
        ]

        labels={
            'username':'Nombre de usuario',
            'first_name':'Nombre',
            'last_name':'Apellidos',
            'email':'Correo Electronico',
            'escuela':'Escuela',
            'rol': 'Rol'
        }


        widgets={
            'username': forms.TextInput(attrs={'class':'form-control','id':'nom_corto', 'placeholder': 'Ingrese el nombre corto de usuario'}),
            'first_name': forms.TextInput(attrs={'class':'form-control','id':'nombre', 'placeholder': 'Ingrese el nombre del usuario'}),
            'last_name': forms.TextInput(attrs={'class':'form-control','id':'apellidos', 'placeholder': 'Ingrese los apellidos del usuario'}),
            'email': forms.EmailInput(attrs={'class':'form-control','id':'email', 'placeholder': 'Ingrese el correo electronico'}),
            'escuela': forms.Select(attrs={'class':'form-control','id':'escuela'}),
            'roles': forms.Select(attrs={'class':'form-control','id':'escuela'}),
        }

class UsuarioForm(forms.ModelForm):

    class Meta:
        model = Usuario

        fields=[
            'username',
            'first_name',
            'last_name',
            'email',
            'escuela',
            'rol'
        ]

        labels={
            'username':'Nombre de usuario',
            'first_name':'Nombre',
            'last_name':'Apellidos',
            'email':'Correo Electronico',
            'escuela':'Escuela',
            'rol': 'Rol'
        }


        widgets={
            'username': forms.TextInput(attrs={'class':'form-control','id':'nom_corto', 'placeholder': 'Ingrese el nombre corto de usuario'}),
            'first_name': forms.TextInput(attrs={'class':'form-control','id':'nombre', 'placeholder': 'Ingrese el nombre del usuario'}),
            'last_name': forms.TextInput(attrs={'class':'form-control','id':'apellidos', 'placeholder': 'Ingrese los apellidos del usuario'}),
            'email': forms.EmailInput(attrs={'class':'form-control','id':'email', 'placeholder': 'Ingrese el correo electronico'}),
            'escuela': forms.Select(attrs={'class':'form-control','id':'escuela'}),
            'roles': forms.Select(attrs={'class':'form-control','id':'escuela'}),
        }


