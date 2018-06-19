from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.password_validation import validate_password

from .models import Usuario, Rol
from escuela.models import Escuela

class UsuarioCreateForm(UserCreationForm):
    error_messages = {
        'duplicate_username': 'Nombre de usuario ya en uso. Ingrese otro',
        'password_mismatch': "Los dos passwords no coinciden.",
    }
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
            'rol': forms.Select(attrs={'class':'form-control','id':'rol'}),
        }

    def clean_username(self):
        username = self.cleaned_data["username"]
       
        try:
            Usuario._default_manager.get(username=username)
            #if the user exists, then let's raise an error message

            raise forms.ValidationError( 
              self.error_messages['duplicate_username'],  #user my customized error message

              code='duplicate_username',   #set the error message key

                )
        except Usuario.DoesNotExist:
            return username # great, this user does not exist so we can continue the registration process
    
    def clean_password1(self):
        password1 = self.cleaned_data.get("password1")
        validate_password(password1)


    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2
    
    def __init__(self, *args, **kwargs):
        super(UsuarioCreateForm, self).__init__(*args, **kwargs)
        self.fields['escuela'].queryset = Escuela.objects.filter(estado=True)
        self.fields['rol'].queryset = Rol.objects.filter(estado=True)



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
            'rol': forms.Select(attrs={'class':'form-control','id':'rol'}),
        }


