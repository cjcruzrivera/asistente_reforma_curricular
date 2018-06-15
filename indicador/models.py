# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from resultado_aprendizaje.models import ResultadoAprendizaje
from actividad.models import Actividad

# Create your models here.

class IndicadorLogro(models.Model):
    descripcion = models.CharField(max_length=250)
    resultado = models.ForeignKey(ResultadoAprendizaje)
    estado = models.BooleanField(default=True)
    actividades = models.ManyToManyField(Actividad)

    def delete(self):
        if self.estado:
            self.estado = False
            self.save()
            return True
        else:
            return False

    def __unicode__(self):
        return '{}'.format(self.descripcion)