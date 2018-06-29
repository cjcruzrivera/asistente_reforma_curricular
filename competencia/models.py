# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from resultado_aprendizaje.models import ResultadoAprendizaje

# Create your models here.

class Competencia(models.Model):
    descripcion = models.CharField(max_length=250)
    curso = models.ForeignKey('curso.Curso')
    estado = models.BooleanField(default=True)

    def validateCompleto(self):
        competencia = Competencia.objects.get(pk=self.id)
        if ResultadoAprendizaje.objects.filter(competencia=competencia, estado=True).exists():
            for resultado in ResultadoAprendizaje.objects.filter(competencia=competencia, estado=True):
                if not resultado.validateCompleto():
                    return False
                
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