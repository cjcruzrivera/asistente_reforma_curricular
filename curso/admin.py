# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Curso, TipoCurso
from competencia.models import Competencia
# Register your models here.

admin.site.register(Curso)
admin.site.register(TipoCurso)

admin.site.register(Competencia)
