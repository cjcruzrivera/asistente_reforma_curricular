# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from programa.models import Programa
from programa.forms import ProgramaForm

# Create your views here.

def index(request):
    render(request, 'programas/index.html')

class ProgramaListView(ListView):
    model = Programa
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
        # Agregamos un QuerySet de todos los books
        context['usuario'] = self.request.user
        return context

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
