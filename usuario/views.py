# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from django.http import JsonResponse
from django.core.urlresolvers import reverse_lazy

from .models import Usuario
from .forms import UsuarioCreateForm, UsuarioForm
from programa.models import Programa

# Create your views here.

def index(request):
    return render(request, 'usuario/index.html')

def consulta_programa(request):
    pk = request.POST.get('id_usuario')
    usuario = Usuario.objects.get(pk=pk)
    programa = Programa.objects.get(dir_programa=usuario)
    response = {'resultado': 'exito','programa':programa.id}
    return JsonResponse(response)



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

def eliminar(request):
    pk = request.POST.get('id_usuario')
    usuario_borrar = Usuario.objects.get(pk=pk)
    if usuario_borrar.delete():
        nombre = usuario_borrar.first_name + " " + usuario_borrar.last_name
        response = {'resultado': 'exito','nombre':nombre}
    else:
        response = {'resultado': 'error'}

    return JsonResponse(response)

class UsuarioDeleteView(DeleteView):
    model = Usuario
    template_name = "usuario/usuario_delete.html"
    success_url = reverse_lazy('usuario:usuario_listar')
