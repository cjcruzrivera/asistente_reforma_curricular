# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import JsonResponse

from .models import Actividad, TipoActividad

# Create your views here.


def editar(request):
    id_actividad = request.POST.get('id_actividad')
    tipo = request.POST.get('tipo')
    descripcion = request.POST.get('descripcion')
    tipo = TipoActividad.objects.get(pk=tipo)
    actividad = Actividad.objects.get(pk=id_actividad)
    actividad.tipo = tipo
    actividad.descripcion = descripcion
    actividad.save()
    response = {'resultado': 'exito'}
    return JsonResponse(response)


def eliminar(request):
    pk = request.POST.get('id_actividad')
    actividad_borrar = Actividad.objects.get(pk=pk)
    if actividad_borrar.delete():
        response = {'resultado': 'exito','nombre':''}
    else:
        response = {'resultado': 'error'}

    return JsonResponse(response)