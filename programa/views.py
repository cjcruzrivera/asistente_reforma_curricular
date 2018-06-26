# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.http import JsonResponse
from django.core import serializers

from .models import Programa
from .forms import ProgramaForm
from usuario.models import Usuario, Rol
from curso.models import Curso
from competencia.models import Competencia
# Create your views here.

def index(request):
    render(request, 'programas/index.html')

def view_one(request, pk):
    programa = Programa.objects.get(pk=pk)
    cursos = Curso.objects.filter(programa=programa)
    return render(request, 'programas/programa_view.html',{
        'programa':programa,
        'usuario': request.user,
        'cursos': cursos,
    })


def reporte(request, pk):
    programa = Programa.objects.get(pk=pk)
    cursos = Curso.objects.filter(programa=programa)
    competencias = Competencia.objects.filter(curso__in=cursos)
    return render(request, 'reportes/reporte_programas.html',{
        'programa':programa,
        'competencias':competencias,
        'usuario': request.user,
    })
 

class ProgramaListView(ListView):
    model = Programa
    queryset = Programa.objects.filter(estado=True)
    template_name = "programas/programa_list.html"

    def get_context_data(self, **kwargs):
        # Llamamos ala implementacion para traer un primer context
        context = super(ProgramaListView, self).get_context_data(**kwargs)
        # Agregamos un QuerySet de todos los books
        context['usuario'] = self.request.user
        return context

class ProgramaCreateView(CreateView):
    model = Programa
    form_class = ProgramaForm
    template_name = "programas/programa_form.html"
    success_url = reverse_lazy('programa:programa_listar')

    def get_context_data(self, **kwargs):
        # Llamamos ala implementacion para traer un primer context
        context = super(ProgramaCreateView, self).get_context_data(**kwargs)
        # Agregamos un QuerySet de todos los books
        context['accion'] = 'Registrar'
        context['usuario'] = self.request.user
        return context

class ProgramaUpdateView(UpdateView):
    model = Programa
    form_class = ProgramaForm
    template_name = "programas/programa_form.html"
    success_url = reverse_lazy('programa:programa_listar')

    def get_context_data(self, **kwargs):
        # Llamamos ala implementacion para traer un primer context
        context = super(ProgramaUpdateView, self).get_context_data(**kwargs)
        context['accion'] = 'Editar'
        context['usuario'] = self.request.user
        return context


def eliminar(request):
    pk = request.POST.get('id_programa')
    programa_borrar = Programa.objects.get(pk=pk)
    if programa_borrar.delete():
        response = {'resultado': 'exito','nombre':programa_borrar.nombre}
    else:
        response = {'resultado': 'error'}

    return JsonResponse(response)


def listar_dir(request):
    id_escuela = request.POST.get('id_escuela')
    if id_escuela == '':
        return JsonResponse({'vacio':'vacio'}, safe=False)

    rol = Rol.objects.get(nombre='Director de Programa')
    pos_directores = Usuario.objects.filter(escuela=id_escuela, rol=rol , estado=True)
    for dire in pos_directores:
        if(dire.is_dir):
            print "SI"
    data = serializers.serialize('json', pos_directores, fields=('id', 'first_name', 'last_name'))

    return JsonResponse(data, safe=False)

class ProgramaDeleteView(DeleteView):
    model = Programa
    form_class = ProgramaForm
    template_name = "programas/programa_delete.html"
    success_url = reverse_lazy('programa:programa_listar')

    def get_context_data(self, **kwargs):
        # Llamamos ala implementacion para traer un primer context
        context = super(ProgramaDeleteView, self).get_context_data(**kwargs)
        # Agregamos un QuerySet de todos los books
        context['usuario'] = self.request.user
        return context
