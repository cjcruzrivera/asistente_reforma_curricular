from django import forms
from programa.models import Programa

class ProgramaForm(forms.ModelForm):
	class Meta:
		model = Programa

		fields=[
			'nombre',
			'semestres',
			'creditos',
			'cod_escuela',
			'dir_programa'
		]

		labels={
			'nombre':'Nombre del Programa',
			'semestres':'Semestres del Programa',
			'creditos':'Numero de Creditos',
			'cod_escuela':'Escuela a la que pertenece',
			'dir_programa':'Director de Programa'
		}

		widgets={
			'nombre': forms.TextInput(attrs={'class':'form-control','id':'nombre', 'placeholder': 'Ingrese el nombre del programa'}),
         		'semestres': forms.TextInput(attrs={'class':'form-control','id':'semestres', 'placeholder': 'Ingrese los semestres del Programa'}),
            		'creditos': forms.TextInput(attrs={'class':'form-control','id':'codigo_escuela', 'placeholder': 'Ingrese el numero de creditos del programa'}),
            		'cod_escuela': forms.Select(attrs={'class':'form-control','id':'escuela'}),
            		'dir_programa': forms.Select(attrs={'class':'form-control','id':'dir_programa'})
		}
