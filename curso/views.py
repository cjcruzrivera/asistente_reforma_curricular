# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.http import JsonResponse

from .models import Curso
from .forms import CursoForm, PrerrequisitosForm
# Create your views here.


def index(request):
    return render(request, 'curso/index.html')

def view_one(request, pk):
    curso = Curso.objects.get(pk=pk)
    prerrequisitos = curso.prerrequisitos.all()
    posibles_pre = Curso.objects.filter(estado=True, semestre__lt=curso.semestre)
    pos = posibles_pre.difference(prerrequisitos)
    return render(request, 'curso/curso_view.html',{
        'curso':curso,
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
    response = {'resultado': 'exito', 'nombre':prerrequis.nombre}
    return JsonResponse(response)

def eliminar(request):
    pk = request.POST.get('id_curso')
    curso_borrar = Curso.objects.get(pk=pk)
    if curso_borrar.delete():
        response = {'resultado': 'exito','nombre':curso_borrar.nombre}
    else:
        response = {'resultado': 'error'}

    return JsonResponse(response)

class CursoListView(ListView):
    model = Curso
    queryset = Curso.objects.filter(estado=True)
    template_name = "curso/curso_list.html"

    def get_context_data(self, **kwargs):
        # Llamamos ala implementacion para traer un primer context
        context = super(CursoListView, self).get_context_data(**kwargs)
        # Agregamos un QuerySet de todos los books
        context['usuario'] = self.request.user
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
        return context


class PrerrequisitosUpdateView(UpdateView):
    model = Curso
    form_class = PrerrequisitosForm
    template_name = "curso/curso_form.html"
    success_url = reverse_lazy('curso:curso_listar')

    def get_context_data(self, **kwargs):
        # Llamamos ala implementacion para traer un primer context
        context = super(PrerrequisitosUpdateView, self).get_context_data(**kwargs)
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
