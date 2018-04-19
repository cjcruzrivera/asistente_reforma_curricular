# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from .models import Escuela
from .forms import EscuelaForm
# Create your views here.


def index(request):
    return render(request, 'escuela/index.html')


class EscuelaListView(ListView):
    model = Escuela
    queryset = Escuela.objects.filter(estado=True)
    template_name = "escuela/escuela_list.html"

class EscuelaCreateView(CreateView):
    model = Escuela
    form_class = EscuelaForm
    template_name = "escuela/escuela_form.html"
    success_url = reverse_lazy('escuela:escuela_listar')

class EscuelaUpdateView(UpdateView):
    model = Escuela
    form_class = EscuelaForm
    template_name = "escuela/escuela_form.html"
    success_url = reverse_lazy('escuela:escuela_listar')

class EscuelaDeleteView(DeleteView):
    model = Escuela
    form_class = EscuelaForm
    template_name = "escuela/escuela_delete.html"
    success_url = reverse_lazy('escuela:escuela_listar')