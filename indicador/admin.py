# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from .models import IndicadorLogro, Evaluaciones

admin.site.register(IndicadorLogro)
admin.site.register(Evaluaciones)

