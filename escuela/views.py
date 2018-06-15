# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.http import JsonResponse

from .models import Escuela
from .forms import EscuelaForm
# Create your views here.


def index(request):
    return render(request, 'escuela/index.html')


class EscuelaListView(ListView):
    model = Escuela
    queryset = Escuela.objects.filter(estado=True)
    template_name = "escuela/escuela_list.html"

    def get_context_data(self, **kwargs):
        # Llamamos ala implementacion para traer un primer context
        context = super(EscuelaListView, self).get_context_data(**kwargs)
        # Agregamos un QuerySet de todos los books
        context['usuario'] = self.request.user
        return context


class EscuelaCreateView(CreateView):
    model = Escuela
    form_class = EscuelaForm
    template_name = "escuela/escuela_form.html"
    success_url = reverse_lazy('escuela:escuela_listar')

    def get_context_data(self, **kwargs):
        # Llamamos ala implementacion para traer un primer context
        context = super(EscuelaCreateView, self).get_context_data(**kwargs)
        # Agregamos un QuerySet de todos los books
        context['usuario'] = self.request.user
        return context


class EscuelaUpdateView(UpdateView):
    model = Escuela
    form_class = EscuelaForm
    template_name = "escuela/escuela_form.html"
    success_url = reverse_lazy('escuela:escuela_listar')

    def get_context_data(self, **kwargs):
        # Llamamos ala implementacion para traer un primer context
        context = super(EscuelaUpdateView, self).get_context_data(**kwargs)
        # Agregamos un QuerySet de todos los books
        context['usuario'] = self.request.user
        return context


def eliminar(request):
    pk = request.POST.get('id_escuela')
    escuela_borrar = Escuela.objects.get(pk=pk)
    if escuela_borrar.delete():
        response = {'resultado': 'exito'}
    else:
        response = {'resultado': 'error'}

    return JsonResponse(response)


class EscuelaDeleteView(DeleteView):
    model = Escuela
    form_class = EscuelaForm
    template_name = "escuela/escuela_delete.html"
    success_url = reverse_lazy('escuela:escuela_listar')

    def get_context_data(self, **kwargs):
        # Llamamos ala implementacion para traer un primer context
        context = super(EscuelaDeleteView, self).get_context_data(**kwargs)
        # Agregamos un QuerySet de todos los books
        context['usuario'] = self.request.user
        return context
