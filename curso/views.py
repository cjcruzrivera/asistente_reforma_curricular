# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from .models import Curso
from .forms import CursoForm
# Create your views here.


def index(request):
    return render(request, 'curso/index.html')


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
