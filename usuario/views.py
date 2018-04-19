# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from .models import Usuario
from .forms import UsuarioCreateForm, UsuarioForm

# Create your views here.

def index(request):
    return render(request, 'usuario/index.html')

class UsuarioListView(ListView):
    model = Usuario
    queryset = Usuario.objects.filter(estado=True)
    template_name = "usuario/usuario_list.html"

class UsuarioCreateView(CreateView):
    model = Usuario
    form_class = UsuarioCreateForm
    template_name = "usuario/usuario_form.html"
    success_url = reverse_lazy('usuario:usuario_listar')

class UsuarioUpdateView(UpdateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = "usuario/usuario_form.html"
    success_url = reverse_lazy('usuario:usuario_listar')

class UsuarioDeleteView(DeleteView):
    model = Usuario
    template_name = "usuario/usuario_delete.html"
    success_url = reverse_lazy('usuario:usuario_listar')
