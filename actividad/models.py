# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class TipoActividad(models.Model):
    nombre = models.CharField(max_length=30)
    estado = models.BooleanField(default=True)

    def delete(self):
        if self.estado:
            self.estado = False
            self.save()
            return True
        else:
            return False

    def __unicode__(self):
        return '{}'.format(self.nombre)
    

class Actividad(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=150)
    tipo = models.ForeignKey(TipoActividad)
    estado = models.BooleanField(default=True)

    def delete(self):
        if self.estado:
            self.estado = False
            self.save()
            return True
        else:
            return False

    def __unicode__(self):
        return '{}'.format(self.nombre)    