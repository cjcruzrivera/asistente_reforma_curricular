from django import forms
from .models import Curso

class CursoForm(forms.ModelForm):

    class Meta:
        model = Curso

        fields=[
            'codigo',
            'nombre',
            'creditos',
            'programa',
            'horas_catedra',
            'horas_individual',
            'semestre',
            'validable',
            'habilitable',
            'tipo',
            'docente_encargado',
        ]

        labels={
            'codigo':'Codigo del Curso',
            'nombre':'Nombre',
            'creditos':'Numero de Creditos',
            'programa':'Programa Academico',
            'horas_catedra':'Horas de Clase Magistral',
            'horas_individual':'Horas de Estudio Independiente',
            'semestre':'Semestre al que pertenece',
            'validable':'Es Validable',
            'habilitable':'Es Habilitable',
            'tipo':'Tipo de Curso',
            'docente_encargado':'Docente Encargado',
        }


        widgets={
            'codigo': forms.TextInput(attrs={'class':'form-control','id':'codigo', 'placeholder': 'Ingrese el codigo del curso'}),
            'nombre': forms.TextInput(attrs={'class':'form-control','id':'nombre', 'placeholder': 'Ingrese el nombre del curso'}),
            'creditos': forms.NumberInput(attrs={'class':'form-control','id':'creditos', 'placeholder': 'Ingrese el numero de creditos del curso'}),
            'programa': forms.Select(attrs={'class':'form-control','id':'programa'}),
            'horas_catedra': forms.NumberInput(attrs={'class':'form-control','id':'horas_magistral', 'placeholder': 'Ingrese el numero de horas de clase magistral'}),
            'horas_individual': forms.NumberInput(attrs={'class':'form-control','id':'creditos', 'placeholder': 'Ingrese el numero de horas de clase independiente'}),
            'semestre': forms.NumberInput(attrs={'class':'form-control','id':'creditos', 'placeholder': 'Ingrese el semestre al que pertenece el curso'}),
            'validable': forms.CheckboxInput(attrs={'class':'form-control','id':'validable'}),
            'habilitable': forms.CheckboxInput(attrs={'class':'form-control','id':'habilitable'}),
            'tipo': forms.Select(attrs={'class':'form-control','id':'tipo'}),
            'docente_encargado':forms.Select(attrs={'class':'form-control','id':'docente'}),
        }



