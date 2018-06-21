# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import UpdateView, CreateView
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect, JsonResponse


from .models import ResultadoAprendizaje
from .forms import ResultadoAprendizajeForm
from competencia.models import Competencia
from curso.models import Curso
from indicador.models import IndicadorLogro
from actividad.models import Actividad, TipoActividad


# Create your views here.

def view_one(request, pk):
    resultadoAprendizaje = ResultadoAprendizaje.objects.get(pk=pk)
    indicadores = IndicadorLogro.objects.filter(resultado=resultadoAprendizaje)
    actividades = resultadoAprendizaje.actividades
    tipos_act = TipoActividad.objects.filter(estado=True)
    return render(request, 'resultado/resultados_view.html',{
        'usuario': request.user,
        'indicadores': indicadores,
        'ResultadoAprendizaje': resultadoAprendizaje,
        # 'actividades': actividades,
        'tipos': tipos_act,
    })

class ResultadoAprendizajeCreateView(CreateView):
    model = ResultadoAprendizaje
    form_class = ResultadoAprendizajeForm
    template_name = "resultado/resultados_form.html"

    def get_context_data(self, **kwargs):
        # Llamamos ala implementacion para traer un primer context
        context = super(ResultadoAprendizajeCreateView, self).get_context_data(**kwargs)
        self.competencia = Competencia.objects.get(pk=self.kwargs['pk'])
        self.curso = Curso.objects.get(pk=self.competencia.curso.id)

        # Agregamos un QuerySet de todos los books
        context['accion'] = 'Registrar'
        context['usuario'] = self.request.user
        context['competencia'] = self.competencia
        context['curso'] = self.curso
        return context
    
    def get_success_url(self, **kwargs):
        self.competencia = Competencia.objects.get(pk=self.kwargs['pk'])
        return reverse_lazy('competencia:view_one', kwargs = {'pk': self.competencia.id})

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.competencia = Competencia.objects.get(pk=self.kwargs['pk'])
        form.save()
        return HttpResponseRedirect(self.get_success_url())

class ResultadoAprendizajeUpdateView(UpdateView):
    model = ResultadoAprendizaje
    form_class = ResultadoAprendizajeForm
    template_name = "resultado/resultados_form.html"

    def get_context_data(self, **kwargs):
        # Llamamos ala implementacion para traer un primer context
        context = super(ResultadoAprendizajeUpdateView, self).get_context_data(**kwargs)
        self.competencia = ResultadoAprendizaje.objects.get(pk=self.kwargs['pk']).competencia
        context['accion'] = 'Editar'
        context['usuario'] = self.request.user
        context['competencia'] = self.competencia

        return context

    def get_success_url(self, **kwargs):
        self.competencia = ResultadoAprendizaje.objects.get(pk=self.kwargs['pk']).competencia
        return reverse_lazy('competencia:view_one', kwargs = {'pk': self.competencia.id})




def eliminar(request):
    pk = request.POST.get('id_resultado')
    resultado_borrar = ResultadoAprendizaje.objects.get(pk=pk)
    if resultado_borrar.delete():
        response = {'resultado': 'exito','nombre':''}
    else:
        response = {'resultado': 'error'}

    return JsonResponse(response)