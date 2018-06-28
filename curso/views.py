# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.http import JsonResponse

from .models import Curso
from .forms import CursoForm, PrerrequisitosForm

from indicador.models import IndicadorLogro
from competencia.models import Competencia
from resultado_aprendizaje.models import ResultadoAprendizaje
# Create your views here.


def index(request):
    return render(request, 'curso/index.html')


def detail(request):
    curso = Curso.objects.get(pk=request.POST.get('id_curso'))
    estado = curso.validateCompleto()
    if estado:
        status = 'COMPLETO'
    else:
        status = "INCOMPLETO"
    comp_completas = 0
    resul_completos = 0
    indic_completos = 0

    competencias = Competencia.objects.filter(curso=curso, estado=True)
    num_competencias = competencias.count()
    if num_competencias != 0:
        for comp in competencias:
            if comp.validateCompleto():
                comp_completas += 1

    resultados = ResultadoAprendizaje.objects.filter(
        competencia__in=competencias, estado=True)
    num_resultados = resultados.count()

    if num_resultados != 0:
        for result in resultados:
            if result.validateCompleto():
                resul_completos += 1

    indicadores = IndicadorLogro.objects.filter(
        resultado__in=resultados, estado=True)
    num_indicadores = indicadores.count()

    if num_indicadores != 0:
        for indi in indicadores:
            if indi.validateCompleto():
                indic_completos += 1
    info_competencias = 'Hay ' + \
        str(num_competencias) + ' competencia/s registrada/s. ' + \
        str(comp_completas) + " completa/s"
    info_resultados = 'Hay ' + \
        str(num_resultados) + ' resultado/s registrado/s. ' + \
        str(comp_completas) + " completo/s"
    info_indicadores = 'Hay ' + \
        str(num_indicadores) + ' indicador/es registrado/s. ' + \
        str(comp_completas) + " completo/s"
    detalles = {'estado': status,
                'competencias': info_competencias,
                'resultados': info_resultados,
                'indicadores': info_indicadores,
                }
    return JsonResponse(detalles, safe=False)


def view_one(request, pk):
    curso = Curso.objects.get(pk=pk)
    prerrequisitos = curso.prerrequisitos.all()
    posibles_pre = Curso.objects.filter(
        estado=True, semestre__lt=curso.semestre)
    pos = posibles_pre.difference(prerrequisitos)
    competencias = Competencia.objects.filter(curso=curso)
    resultados = ResultadoAprendizaje.objects.filter(
        competencia__in=competencias)
    reporte = IndicadorLogro.objects.filter(resultado__in=resultados)
    return render(request, 'curso/curso_view.html', {
        'curso': curso,
        'reporte': reporte,
        'usuario': request.user,
        'prerrequisitos': prerrequisitos,
        'posibles_pre': pos,
    })


def prerrequisito(request):
    id_curso = request.POST.get('id_curso')
    id_pre = request.POST.get('id_pre')
    curso = Curso.objects.get(pk=id_curso)
    prerrequis = Curso.objects.get(pk=id_pre)
    curso.prerrequisitos.add(prerrequis)
    curso.save()
    response = {'resultado': 'exito', 'nombre': prerrequis.nombre}
    return JsonResponse(response)


def eliminar(request):
    pk = request.POST.get('id_curso')
    curso_borrar = Curso.objects.get(pk=pk)
    if curso_borrar.delete():
        response = {'resultado': 'exito', 'nombre': curso_borrar.nombre}
    else:
        response = {'resultado': 'error'}

    return JsonResponse(response)


def eliminar_pre(request):
    id_borrar = request.POST.get('id_borrar')
    id_borrar = id_borrar.split('-')
    id_pre = id_borrar[0]
    id_curso = id_borrar[1]
    pre = Curso.objects.get(pk=id_pre)
    curso = Curso.objects.get(pk=id_curso)
    curso.prerrequisitos.remove(pre)
    response = {'resultado': 'exito', 'nombre': pre.nombre}

    return JsonResponse(response)


class CursoListView(ListView):
    model = Curso
    template_name = "curso/curso_list.html"

    def get_queryset(self):
        usuario = self.request.user
        if usuario.rol.nombre == 'Docente':
            cursos = Curso.objects.filter(docente_encargado=usuario)
        else:
            cursos = Curso.objects.all()
        for curso in cursos:
            curso.completo = curso.validateCompleto()
        return cursos

    def get_context_data(self, **kwargs):
        # Llamamos ala implementacion para traer un primer context
        context = super(CursoListView, self).get_context_data(**kwargs)
        usuario = self.request.user
        context['usuario'] = usuario
        return context


class CursoCreateView(CreateView):
    model = Curso
    form_class = CursoForm
    template_name = "curso/curso_form.html"
    success_url = reverse_lazy('curso:curso_listar')

    def get_context_data(self, **kwargs):
        # Llamamos ala implementacion para traer un primer context
        context = super(CursoCreateView, self).get_context_data(**kwargs)
        # Agregamos un QuerySet de todos los books
        context['usuario'] = self.request.user
        context['accion'] = 'Registrar'
        return context


class CursoUpdateView(UpdateView):
    model = Curso
    form_class = CursoForm
    template_name = "curso/curso_form.html"
    success_url = reverse_lazy('curso:curso_listar')

    def get_context_data(self, **kwargs):
        # Llamamos ala implementacion para traer un primer context
        context = super(CursoUpdateView, self).get_context_data(**kwargs)
        # Agregamos un QuerySet de todos los books
        context['usuario'] = self.request.user
        context['accion'] = 'Editar'
        return context


class PrerrequisitosUpdateView(UpdateView):
    model = Curso
    form_class = PrerrequisitosForm
    template_name = "curso/curso_form.html"
    success_url = reverse_lazy('curso:curso_listar')

    def get_context_data(self, **kwargs):
        # Llamamos ala implementacion para traer un primer context
        context = super(PrerrequisitosUpdateView,
                        self).get_context_data(**kwargs)
        # Agregamos un QuerySet de todos los books
        context['usuario'] = self.request.user
        return context


class CursoDeleteView(DeleteView):
    model = Curso
    form_class = CursoForm
    template_name = "curso/curso_delete.html"
    success_url = reverse_lazy('curso:curso_listar')

    def get_context_data(self, **kwargs):
        # Llamamos ala implementacion para traer un primer context
        context = super(CursoDeleteView, self).get_context_data(**kwargs)
        # Agregamos un QuerySet de todos los books
        context['usuario'] = self.request.user
        return context
