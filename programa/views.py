# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from programa.models import Programa
from programa.forms import ProgramaForm

# Create your views here.

def index(request):
	return render(request, 'programas/index.html')

class ProgramaListView(ListView):
	model = Programa
	template_name = "programas/programa_list.html"

class ProgramaCreateView(CreateView):
	model = Programa
	form_class = ProgramaForm
	template_name = "programas/programa_form.html"
	success_url = reverse_lazy('programas:programa_listar')

class ProgramaUpdateView(UpdateView):
    	model = Programa
    	form_class = ProgramaForm
   	template_name = "programas/programa_form.html"
    	success_url = reverse_lazy('programas:programa_listar')

class ProgramaDeleteView(DeleteView):
    	model = Programa
    	form_class = ProgramaForm
    	template_name = "programas/programa_delete.html"
    	success_url = reverse_lazy('programas:programa_listar')
