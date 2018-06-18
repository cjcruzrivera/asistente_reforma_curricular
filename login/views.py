# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from usuario.models import Rol
from actividad.models import TipoActividad
from escuela.models import Escuela
from curso.models import TipoCurso

# Create your views here.

@login_required(login_url='/')
def index(request):
    usuario = request.user
    return render(request,'index.html' ,{'usuario': usuario})


def carga_datos_inicial(request):
    roles = ['Docente', 'Decano', 'Director de Programa', 'Administrador']
    tipos_act = ['Formacion', 'Evaluacion']
    tipos_cursos = ['Asignatura básica', 'Asignatura Profesional', 'Electiva Complementaria', 'Electiva Profesional']
    escuelas = [{'corto':'EISC','largo':'Escuela de Ingenieria en Sistemas y Computacion'},
                {'corto':'EIEE','largo':'Escuela de Ingeniería Eléctrica y Electrónica'},
                {'corto':'EICG','largo':'Escuela de Ingeniería Civil y Geomática'},
                {'corto':'EIDENAR','largo':'Escuela de Ingenieria de Recursos Naturales y del Ambiente'},]
    usuarios = [{'username':'raul_g', 'first_name':'Raul','last_name':'Gutierrez', 'rol': 'Director de Programa'}]
    for escuela in escuelas:
        if not Escuela.objects.filter(nombre_corto=escuela['corto']).exists():
            registro= Escuela(nombre_largo=escuela['largo'],nombre_corto=escuela['corto'])
            registro.save()

    for rol in roles:
        if not Rol.objects.filter(nombre=rol).exists():
            registro = Rol(nombre=rol)
            registro.save()
   
    for tipo in tipos_act:
        if not TipoActividad.objects.filter(nombre=tipo).exists():
            registro = TipoActividad(nombre=tipo)
            registro.save()

    for tipo in tipos_cursos:
        if not TipoCurso.objects.filter(nombre=tipo).exists():
            registro = TipoCurso(nombre=tipo)
            registro.save()
            
    return HttpResponse("Datos Cargados")