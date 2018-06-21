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
    escuelas = [{'corto':'EISC','largo':'Escuela de Ingeniería en Sistemas y Computacion'},
                {'corto':'EIEE','largo':'Escuela de Ingeniería Eléctrica y Electrónica'},
                {'corto':'EICG','largo':'Escuela de Ingeniería Civil y Geomática'},
                {'corto': 'Estad', 'largo': 'Escuela de Estadística'},
                {'corto':'EIDENAR','largo':'Escuela de Ingeniería de Recursos Naturales y del Ambiente'}]

    usuarios = [{'username':'raul_g', 'first_name':'Raul','last_name':'Gutierrez', 'rol': 'Director de Programa', 'password':'eisc_dir', 'email':'raul_g@eisc.com', 'escuela': 'EISC'},
                {'username': 'mauricio_f', 'first_name': 'Mauricio Eduardo', 'last_name': 'Fernández', 'rol': 'Director de Programa', 'password': 'eisc_dir', 'email': 'mauricio_f@eisc.com', 'escuela': 'EISC'},
                {'username':'diego_g', 'first_name':'Diego Fernando','last_name':'Garcia', 'rol': 'Director de Programa', 'password':'eiee_dir', 'email':'diego_g@eiee.com', 'escuela': 'EIEE'},
                {'username': 'jaime_m', 'first_name': 'Jaime', 'last_name': 'Mosquera Restrepo', 'rol': 'Director de Programa', 'password': 'ee_dir', 'email': 'jaime.mosquera@ee.com', 'escuela': 'Estad'},
                {'username':'hernando_p', 'first_name':'Hernando','last_name':'Palacios', 'rol': 'Director de Programa', 'password':'eiee_dir', 'email':'hernando.palaios@eiee.com', 'escuela': 'EIEE'},
                {'username':'jesus_g', 'first_name':'Jesus','last_name':'Gonzales', 'rol': 'Director de Programa', 'password':'eiee_dir', 'email':'jesus.gonzales@eiee.com', 'escuela': 'EIEE'},
                {'username':'manolo_g', 'first_name':'Manolo','last_name':'Galvan', 'rol': 'Director de Programa', 'password':'eiee_dir', 'email':'manolo_g@eiee.com', 'escuela': 'EIEE'},
                {'username':'luz_b', 'first_name':'Luz Edith','last_name':'Barba', 'rol': 'Director de Programa', 'password':'eiee_dir', 'email':'luz_barba@eiee.com', 'escuela': 'EIDENAR'},
                {'username':'cjcruzrivera', 'first_name':'Camilo José','last_name':'Cruz Rivera', 'rol': 'Administrador', 'password':'admin_cj', 'email':'cjcruzrivera@eisc.com', 'escuela': 'EISC'},
                {'username':'beatriz_f', 'first_name':'Beatriz','last_name':'Florian', 'rol': 'Docente', 'password':'eisc_1234', 'email':'beatriz_f@eisc.com', 'escuela': 'EISC'},
                {'username': 'Roberto_b', 'first_name': 'Roberto', 'last_name': 'Behar Gutierrez', 'rol': 'Docente', 'password': 'behar_1234', 'email': 'roberto.behar@ee.com', 'escuela': 'Estad'},
                {'username': 'Víctor_M', 'first_name': 'Víctor Manuel', 'last_name': 'Gonzales Rojas', 'rol': 'Docente', 'password': 'gonzales_1234', 'email': 'victor.m.gonzales@ee.com', 'escuela': 'Estad'},
                {'username': 'Angel_G', 'first_name': 'Angel', 'last_name': 'Garcia Baños', 'rol': 'Docente', 'password': 'garcia_1234', 'email': 'angel.garcia@eisc.com', 'escuela': 'EISC'},
                {'username': 'Oscar_B', 'first_name': 'Oscar Fernando', 'last_name': 'Bedoya', 'rol': 'Docente', 'password': 'bedoya_1234', 'email': 'oscar.bedoya@eisc.com', 'escuela': 'EISC'},
                {'username': 'Ruben_N', 'first_name': 'Ruben', 'last_name': 'Nieto', 'rol': 'Docente', 'password': 'nieto_1234', 'email': 'ruben.nieto@eiee.com', 'escuela': 'EIEE'},
                {'username': 'Sandra_N', 'first_name': 'Sandra', 'last_name': 'Nope', 'rol': 'Docente', 'password': 'nope_1234', 'email': 'sandra.nope@eiee.com', 'escuela': 'EIEE'},
                {'username':'carlos_loz', 'first_name':'Carlos Arturo','last_name':'Lozano Moncada', 'rol': 'Decano', 'password':'eisc_1234', 'email':'carlos_loz@eisc.com', 'escuela': 'EISC'}]
    
    programas = [{'nombre':'Ingeniería en Sistemas',
                  'semestres': 10,
                  'creditos': 159,
                  'escuela': 'EISC',
                  'dir_programa': 'raul_g'},
                 {'nombre': 'Estadística',
                  'semestres': 10,
                  'creditos': 153,
                  'escuela': 'Estad',
                  'dir_programa': 'jaime_m'},
                 {'nombre': 'Tecnología en Sistemas de Información',
                  'semestres': 7,
                  'creditos': 90,
                  'escuela': 'EISC',
                  'dir_programa': 'mauricio_f'},
                 {'nombre': 'Ingeniería Eléctrica',
                  'semestres': 10,
                  'creditos': 167,
                  'escuela': 'EIEE',
                  'dir_programa': 'diego_g'},
                 {'nombre': 'Ingeniería Electrónica',
                  'semestres': 10,
                  'creditos': 160,
                  'escuela': 'EIEE',
                  'dir_programa': 'hernando_p'},
                 {'nombre': 'Tecnología Electrónica',
                  'semestres': 6,
                  'creditos': 90,
                  'escuela': 'EIEE',
                  'dir_programa': 'jesus_g'},
                 {'nombre': 'Ingeniería Civil',
                  'semestres': 10,
                  'creditos': 170,
                  'escuela': 'EICG',
                  'dir_programa': 'manolo_g'},
                 {'nombre': 'Ingeniería Sanitaria y Ambiental',
                  'semestres': 10,
                  'creditos': 169,
                  'escuela': 'EIDENAR',
                  'dir_programa': 'luz_b'}]

    cursos = [{'nombre':'Desarrollo de Software 2',
               'codigo': '750092M',
               'creditos':4, 
               'programa': 'Ingeniería en Sistemas', 
               'horas_catedra': 4, 
               'horas_individual':8, 
               'tipo':'Asignatura Profesional', 
               'docente_encargado': 'beatriz_f', 
               'semestre':7,
               'validable':True, 
               'habilitable':False},
              {'nombre': 'Sistemas de Información',
               'codigo': '750022M',
               'creditos': 3,
               'programa': 'Ingeniería en Sistemas',
               'horas_catedra': 3,
               'horas_individual': 6,
               'tipo': 'Asignatura Profesional',
               'docente_encargado': 'beatriz_f',
               'semestre': 8,
               'validable': True,
               'habilitable': False},
              {'nombre': 'Inteligencia Artificial',
               'codigo': '750033M',
               'creditos': 4,
               'programa': 'Ingeniería en Sistemas',
               'horas_catedra': 4,
               'horas_individual': 8,
               'tipo': 'Asignatura Profesional',
               'docente_encargado': 'Oscar_B',
               'semestre': 7,
               'validable': True,
               'habilitable': False},
              {'nombre': 'Fundamentos de Analisi y Diseño de Algoritmos',
               'codigo': '750094M',
               'creditos': 4,
               'programa': 'Ingeniería en Sistemas',
               'horas_catedra': 4,
               'horas_individual': 8,
               'tipo': 'Asignatura Profesional',
               'docente_encargado': 'Oscar_B',
               'semestre': 5,
               'validable': True,
               'habilitable': False},
              {'nombre': 'Fundamentos de Lenguajes de Programación',
               'codigo': '750095M',
               'creditos': 4,
               'programa': 'Ingeniería en Sistemas',
               'horas_catedra': 4,
               'horas_individual': 8,
               'tipo': 'Asignatura Profesional',
               'docente_encargado': 'Oscar_B',
               'semestre': 4,
               'validable': True,
               'habilitable': False},
              {'nombre': 'Introducción a la Estadística',
               'codigo': '770087M',
               'creditos': 3,
               'programa': 'Estadística',
               'horas_catedra': 3,
               'horas_individual': 6,
               'tipo': 'Asignatura Profesional',
               'docente_encargado': 'Roberto_b',
               'semestre': 1,
               'validable': True,
               'habilitable': False},
              {'nombre': 'Estadística Descriptiva',
               'codigo': '770086M',
               'creditos': 3,
               'programa': 'Estadística',
               'horas_catedra': 3,
               'horas_individual': 6,
               'tipo': 'Asignatura Profesional',
               'docente_encargado': 'Roberto_b',
               'semestre': 2,
               'validable': True,
               'habilitable': False},
              {'nombre': 'Estadística Aplicada 2',
               'codigo': '790012M',
               'creditos': 4,
               'programa': 'Estadística',
               'horas_catedra': 4,
               'horas_individual': 8,
               'tipo': 'Asignatura Profesional',
               'docente_encargado': 'Roberto_b',
               'semestre': 8,
               'validable': True,
               'habilitable': False},
              {'nombre': 'Muestreo Estadístico',
               'codigo': '770546M',
               'creditos': 4,
               'programa': 'Estadística',
               'horas_catedra': 4,
               'horas_individual': 8,
               'tipo': 'Asignatura Profesional',
               'docente_encargado': 'Víctor_M',
               'semestre': 7,
               'validable': True,
               'habilitable': False},
              {'nombre': 'Introduccion a la Programación Orientada a Objetos',
               'codigo': '750569M',
               'creditos': 3,
               'programa': 'Ingeniería en Sistemas',
               'horas_catedra': 3,
               'horas_individual': 6,
               'tipo': 'Asignatura Profesional',
               'docente_encargado': 'Angel_G',
               'semestre': 7,
               'validable': True,
               'habilitable': False},
              {'nombre': 'Bases de datos',
               'codigo': '750091M',
               'creditos': 4,
               'programa': 'Ingeniería en Sistemas',
               'horas_catedra': 4,
               'horas_individual': 8,
               'tipo': 'Asignatura Profesional',
               'docente_encargado': 'Angel_G',
               'semestre': 6,
               'validable': True,
               'habilitable': False},
              {'nombre': 'Teoria Electromagnética',
               'codigo': '710023M',
               'creditos': 4,
               'programa': 'Ingeniería Eléctrica',
               'horas_catedra': 4,
               'horas_individual': 8,
               'tipo': 'Asignatura Profesional',
               'docente_encargado': 'Ruben_N',
               'semestre': 6,
               'validable': True,
               'habilitable': False},
              {'nombre': 'Circuitos Integrados',
               'codigo': '710568M',
               'creditos': 4,
               'programa': 'Ingeniería Electrónica',
               'horas_catedra': 4,
               'horas_individual': 8,
               'tipo': 'Asignatura Profesional',
               'docente_encargado': 'Ruben_N',
               'semestre': 2,
               'validable': True,
               'habilitable': False},
              {'nombre': 'Electricidad para Electrónica',
               'codigo': '711064M',
               'creditos': 3,
               'programa': 'Ingeniería Electrónica',
               'horas_catedra': 3,
               'horas_individual': 6,
               'tipo': 'Asignatura Profesional',
               'docente_encargado': 'Ruben_N',
               'semestre': 2,
               'validable': True,
               'habilitable': False},
              {'nombre': 'Estadística no Parametrica',
               'codigo': '781546M',
               'creditos': 4,
               'programa': 'Estadística',
               'horas_catedra': 4,
               'horas_individual': 8,
               'tipo': 'Asignatura Profesional',
               'docente_encargado': 'Víctor_M',
               'semestre': 7,
               'validable': True,
               'habilitable': False},
              {'nombre': 'Circuitos Electricos',
               'codigo': '728564M',
               'creditos': 3,
               'programa': 'Ingeniería Eléctrica',
               'horas_catedra': 3,
               'horas_individual': 6,
               'tipo': 'Asignatura Profesional',
               'docente_encargado': 'Sandra_N',
               'semestre': 5,
               'validable': True,
               'habilitable': False},
              {'nombre': 'Electrónica',
               'codigo': '726498M',
               'creditos': 4,
               'programa': 'Ingeniería Eléctrica',
               'horas_catedra': 4,
               'horas_individual': 8,
               'tipo': 'Asignatura Profesional',
               'docente_encargado': 'Sandra_N',
               'semestre': 6,
               'validable': True,
               'habilitable': False},
              {'nombre': 'Transformadores',
               'codigo': '726571M',
               'creditos': 4,
               'programa': 'Ingeniería Eléctrica',
               'horas_catedra': 4,
               'horas_individual': 8,
               'tipo': 'Asignatura Profesional',
               'docente_encargado': 'Sandra_N',
               'semestre': 7,
               'validable': True,
               'habilitable': False},
              {'nombre': 'Lineas y Redes',
               'codigo': '724591M',
               'creditos': 4,
               'programa': 'Ingeniería Eléctrica',
               'horas_catedra': 4,
               'horas_individual': 8,
               'tipo': 'Asignatura Profesional',
               'docente_encargado': 'Sandra_N',
               'semestre': 8,
               'validable': True,
               'habilitable': False}]
    
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