# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import UpdateView, CreateView
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect, JsonResponse

from .models import IndicadorLogro
from .forms import IndicadorForm
from resultado_aprendizaje.models import ResultadoAprendizaje
# Create your views here.

def view_one(request, pk):
    indicador = IndicadorLogro.objects.get(pk=pk)
    return render(request, 'indicador/indicador_view.html',{
        'usuario': request.user,
        'indicador': indicador,
    })

def eliminar(request):
    pk = request.POST.get('id_indicador')
    indicador_borrar = IndicadorLogro.objects.get(pk=pk)
    if indicador_borrar.delete():
        response = {'indicador': 'exito','nombre':''}
    else:
        response = {'indicador': 'error'}

    return JsonResponse(response)


class IndicadorCreateView(CreateView):
    model = IndicadorLogro
    form_class = IndicadorForm
    template_name = "indicador/indicador_form.html"

    def get_context_data(self, **kwargs):
        # Llamamos ala implementacion para traer un primer context
        context = super(IndicadorCreateView, self).get_context_data(**kwargs)
        self.resultadoAprendizaje = ResultadoAprendizaje.objects.get(pk=self.kwargs['pk'])

        # Agregamos un QuerySet de todos los books
        context['accion'] = 'Registrar'
        context['resultado'] = self.resultadoAprendizaje
        context['usuario'] = self.request.user
        return context
    
    def get_success_url(self, **kwargs):
        self.resultadoAprendizaje = ResultadoAprendizaje.objects.get(pk=self.kwargs['pk'])
        return reverse_lazy('resultado:view_one', kwargs = {'pk': self.resultadoAprendizaje.id})

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.resultado = ResultadoAprendizaje.objects.get(pk=self.kwargs['pk'])
        form.save()
        return HttpResponseRedirect(self.get_success_url())


class IndicadorUpdateView(UpdateView):
    model = IndicadorLogro
    form_class = IndicadorForm
    template_name = "indicador/indicador_form.html"

    def get_context_data(self, **kwargs):
        # Llamamos ala implementacion para traer un primer context
        context = super(IndicadorUpdateView, self).get_context_data(**kwargs)
        self.resultadoAprendizaje = IndicadorLogro.objects.get(pk=self.kwargs['pk']).resultado

        # Agregamos un QuerySet de todos los books
        context['accion'] = 'Editar'
        context['resultado'] = self.resultadoAprendizaje
        context['usuario'] = self.request.user
        return context
    
    def get_success_url(self, **kwargs):
        self.resultadoAprendizaje = IndicadorLogro.objects.get(pk=self.kwargs['pk']).resultado
        return reverse_lazy('resultado:view_one', kwargs = {'pk': self.resultadoAprendizaje.id})

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.resultado = IndicadorLogro.objects.get(pk=self.kwargs['pk']).resultado
        form.save()
        return HttpResponseRedirect(self.get_success_url())