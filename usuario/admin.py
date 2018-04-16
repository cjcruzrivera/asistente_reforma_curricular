# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Usuario, Rol, Semestre, User_Rol
# Register your models here.

admin.site.register(Usuario)
admin.site.register(Rol)
admin.site.register(User_Rol)
admin.site.register(Semestre)
