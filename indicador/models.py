# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from actividad.models import Actividad

# Create your models here.

class IndicadorLogro(models.Model):
    habilidades = (('Distingue','Distingue'),('Analiza', 'Analiza'), ('Reconoce','Reconoce'), ('Resuelve','Resuelve'), ('Genera','Genera'), ('Asimila','Asimila'),('Retroalimenta', 'Retroalimenta'))
    habilidad = models.CharField(max_length=250, choices=habilidades)
    contenido = models.CharField(max_length=250)
    contexto = models.CharField(max_length=250)
    resultado = models.ForeignKey('resultado_aprendizaje.ResultadoAprendizaje')
    estado = models.BooleanField(default=True)
    actividades = models.ManyToManyField(Actividad)

    def validateCompleto(self):
        if self.actividades.all():
            return True
        else:
            return False

    def delete(self):
        if self.estado:
            self.estado = False
            self.save()
            return True
        else:
            return False

    def __unicode__(self):
        return '{}'.format(self.descripcion)