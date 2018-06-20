# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from usuario.models import Rol
from actividad.models import TipoActividad
from escuela.models import Escuela
from curso.models import TipoCurso
from usuario.models import Usuario
from curso.models import Curso
from programa.models import Programa

# Create your views here.

@login_required(login_url='/login')
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
    usuarios = [{'username':'raul_g', 'first_name':'Raul','last_name':'Gutierrez', 'rol': 'Director de Programa', 'password':'eisc_dir', 'email':'raul_g@eisc.com', 'escuela': 'EISC'},
                {'username':'diego_g', 'first_name':'Diego Fernando','last_name':'Garcia', 'rol': 'Director de Programa', 'password':'eiee_dir', 'email':'diego_g@eiee.com', 'escuela': 'EIEE'},
                {'username':'cjcruzrivera', 'first_name':'Camilo José','last_name':'Cruz Rivera', 'rol': 'Administrador', 'password':'admin_cj', 'email':'cjcruzrivera@eisc.com', 'escuela': 'EISC'},
                {'username':'beatriz_f', 'first_name':'Beatriz','last_name':'Florian', 'rol': 'Docente', 'password':'eisc_1234', 'email':'beatriz_f@eisc.com', 'escuela': 'EISC'},
                {'username':'carlos_loz', 'first_name':'Carlos Arturo','last_name':'Lozano Moncada', 'rol': 'Decano', 'password':'eisc_1234', 'email':'carlos_loz@eisc.com', 'escuela': 'EISC'},]
    
    programas = [{'nombre':'Ingenieria en Sistemas',
                  'semestres': 10,
                  'creditos': 159,
                  'escuela': 'EISC',
                  'dir_programa': 'raul_g'}]

    cursos = [{'nombre':'Desarrollo de Software 2',
               'codigo': '750092M',
               'creditos':4, 
               'programa': 'Ingenieria en Sistemas', 
               'horas_catedra': 4, 
               'horas_individual':8, 
               'tipo':'Asignatura Profesional', 
               'docente_encargado': 'beatriz_f', 
               'semestre':7,
               'validable':True, 
               'habilitable':False},]
    
    for escuela in escuelas:
        if not Escuela.objects.filter(nombre_corto=escuela['corto']).exists():
            registro= Escuela(nombre_largo=escuela['largo'],nombre_corto=escuela['corto'])
            registro.save()

    for rol in roles:
        if not Rol.objects.filter(nombre=rol).exists():
            registro = Rol(nombre=rol)
            registro.save()

    for usuario in usuarios:
        if not Usuario.objects.filter(username=usuario['username']).exists():
            registro = Usuario.objects.create_user(username=usuario['username'],
                                 email=usuario['email'],
                                 password=usuario['password'])
            registro.first_name = usuario['first_name']
            registro.last_name = usuario['last_name']
            registro.rol = Rol.objects.get(nombre=usuario['rol'])
            registro.escuela = Escuela.objects.get(nombre_corto=usuario['escuela'])
                            #    rol=Rol.objects.get(nombre=usuario['rol']), 
                            #    escuela=Escuela.objects.get(nombre_corto=usuario['escuela']))
            registro.save()
   
    for tipo in tipos_act:
        if not TipoActividad.objects.filter(nombre=tipo).exists():
            registro = TipoActividad(nombre=tipo)
            registro.save()

    for tipo in tipos_cursos:
        if not TipoCurso.objects.filter(nombre=tipo).exists():
            registro = TipoCurso(nombre=tipo)
            registro.save()

    for programa in programas:
        if not Programa.objects.filter(nombre=programa['nombre']).exists():
            registro = Programa(nombre=programa['nombre'],
                                semestres=programa['semestres'],
                                creditos=programa['creditos'],
                                cod_escuela= Escuela.objects.get(nombre_corto=programa['escuela']),
                                dir_programa=Usuario.objects.get(username=programa['dir_programa']),)
            registro.save()

    for curso in cursos:
        if not Curso.objects.filter(codigo=curso['codigo']).exists():
            registro = Curso(codigo=curso['codigo'],
                            nombre=curso['nombre'],
                            creditos=curso['creditos'],
                            horas_catedra=curso['horas_catedra'],
                            horas_individual=curso['horas_individual'],
                            programa=Programa.objects.get(nombre=curso['programa']),
                            tipo=TipoCurso.objects.get(nombre=curso['tipo']),
                            docente_encargado=Usuario.objects.get(username=curso['docente_encargado']), 
                            semestre=curso['semestre'], 
                            validable=curso['validable'], 
                            habilitable=curso['habilitable'],)
            registro.save()

    return HttpResponse("Datos Cargados")