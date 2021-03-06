from django import forms
from .models import Curso, TipoCurso
from usuario.models import Usuario, Rol
from programa.models import Programa

class PrerrequisitosForm(forms.ModelForm):

    class Meta:
        model = Curso

        fields=[
            'nombre',
            'prerrequisitos'
        ]
        
        labels={
            'nombre':'Nombre Curso',
            'prerrequisitos':'Prerrequisitos',
        }
        widgets={
            'nombre': forms.TextInput(attrs={'class':'form-control','id':'nombre','readonly':'true', 'placeholder': 'Ingrese el nombre del curso'}),
            'prerrequisitos': forms.CheckboxSelectMultiple(),
        }



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
            'horas_individual': forms.NumberInput(attrs={'class':'form-control','id':'horas_independientes', 'placeholder': 'Ingrese el numero de horas de clase independiente'}),
            'semestre': forms.NumberInput(attrs={'class':'form-control','id':'semestre', 'placeholder': 'Ingrese el semestre al que pertenece el curso'}),
            'validable': forms.CheckboxInput(attrs={'class':'form-control','id':'validable'}),
            'habilitable': forms.CheckboxInput(attrs={'class':'form-control','id':'habilitable'}),
            'tipo': forms.Select(attrs={'class':'form-control','id':'tipo'}),
            'docente_encargado':forms.Select(attrs={'class':'form-control','id':'docente'}),
        }
    
    def __init__(self, *args, **kwargs):
        super(CursoForm, self).__init__(*args, **kwargs)
        self.fields['programa'].queryset = Programa.objects.filter(estado=True)
        rol = Rol.objects.get(nombre='Docente')
        self.fields['docente_encargado'].queryset = Usuario.objects.filter(estado=True, rol=rol)
        self.fields['tipo'].queryset = TipoCurso.objects.filter(estado=True)




