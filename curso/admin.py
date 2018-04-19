# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Curso, Tipo_Curso

# Register your models here.

admin.site.register(Curso)
admin.site.register(Tipo_Curso)