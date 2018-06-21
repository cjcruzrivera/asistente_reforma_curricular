# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from competencia.models import Competencia
from actividad.models import Actividad
# Create your models here.

class ResultadoAprendizaje(models.Model):
    verbos = (('Distingue','Distingue'),('Describe','Describe'),('Analiza', 'Analiza'), ('Reconoce','Reconoce'), ('Resuelve','Resuelve'), ('Genera','Genera'), ('Asimila','Asimila'),('Retroalimenta', 'Retroalimenta'))
    verbo = models.CharField(max_length=250, choices=verbos)
    contenido = models.CharField(max_length=250)
    contexto  = models.CharField(max_length=250)
    proposito = models.CharField(max_length=250)
    competencia = models.ForeignKey(Competencia, blank=True)
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
