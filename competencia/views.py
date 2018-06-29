# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import ListView, UpdateView, CreateView
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect, JsonResponse

from .models import Competencia
from .forms import CompetenciaForm
from curso.models import Curso
from resultado_aprendizaje.models import ResultadoAprendizaje

# Create your views here.

def view_one(request, pk):
    competencia = Competencia.objects.get(pk=pk)
    resultados = ResultadoAprendizaje.objects.filter(competencia=competencia)
    for resultado in resultados:
        resultado.completo = resultado.validateCompleto()
    return render(request, 'competencias/competencia_view.html',{
        'usuario': request.user,
        'competencia': competencia,
        'resultados': resultados,
    })

class CompetenciaCreateView(CreateView):
    model = Competencia
    form_class = CompetenciaForm
    template_name = "competencias/competencia_form.html"

    def get_context_data(self, **kwargs):
        # Llamamos ala implementacion para traer un primer context
        context = super(CompetenciaCreateView, self).get_context_data(**kwargs)
        self.curso = Curso.objects.get(pk=self.kwargs['pk'])

        # Agregamos un QuerySet de todos los books
        context['accion'] = 'Registrar'
        context['usuario'] = self.request.user
        context['curso'] = self.curso
        return context
    
    def get_success_url(self, **kwargs):
        return reverse_lazy('curso:view', kwargs = {'pk': self.kwargs['pk']})

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.curso = Curso.objects.get(pk=self.kwargs['pk'])
        form.save()
        return HttpResponseRedirect(self.get_success_url())


class CompetenciaUpdateView(UpdateView):
    model = Competencia
    form_class = CompetenciaForm
    template_name = "competencias/competencia_form.html"

    def get_context_data(self, **kwargs):
        # Llamamos ala implementacion para traer un primer context
        context = super(CompetenciaUpdateView, self).get_context_data(**kwargs)
        self.curso = Curso.objects.get(pk=self.kwargs['course'])

        # Agregamos un QuerySet de todos los books
        context['accion'] = 'Editar'
        context['usuario'] = self.request.user
        context['curso'] = self.curso
        return context
    
    def get_success_url(self, **kwargs):
        return reverse_lazy('competencia:competencia_listar', kwargs = {'pk': self.kwargs['course']})

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.curso = Curso.objects.get(pk=self.kwargs['course'])
        form.save()
        return HttpResponseRedirect(self.get_success_url())



def eliminar(request):
    pk = request.POST.get('id_competencia')
    competencia_borrar = Competencia.objects.get(pk=pk)
    if competencia_borrar.delete():
        response = {'resultado': 'exito','nombre':competencia_borrar.descripcion}
    else:
        response = {'resultado': 'error'}

    return JsonResponse(response)

class CompetenciaListView(ListView):
    model = Competencia
    template_name = "competencias/competencia_list.html"
    
    def get_queryset(self):
        self.curso = Curso.objects.get(pk=self.kwargs['pk'])
        competencias = Competencia.objects.filter(curso=self.curso)
        for competencia in competencias:
            competencia.completo = competencia.validateCompleto()
        return competencias

    def get_context_data(self, **kwargs):
        # Llamamos ala implementacion para traer un primer context
        context = super(CompetenciaListView, self).get_context_data(**kwargs)
        # Agregamos un QuerySet de todos los books
        context['usuario'] = self.request.user
        context['curso'] = self.curso
        return context