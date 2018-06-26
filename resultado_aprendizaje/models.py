# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from actividad.models import Actividad
from indicador.models import IndicadorLogro
# Create your models here.

class ResultadoAprendizaje(models.Model):
    verbos = (('Distingue','Distingue'),('Describe','Describe'),('Analiza', 'Analiza'), ('Reconoce','Reconoce'), ('Resuelve','Resuelve'), ('Genera','Genera'), ('Asimila','Asimila'),('Retroalimenta', 'Retroalimenta'))
    verbo = models.CharField(max_length=250, choices=verbos)
    contenido = models.CharField(max_length=250)
    contexto  = models.CharField(max_length=250)
    proposito = models.CharField(max_length=250)
    competencia = models.ForeignKey('competencia.Competencia', blank=True)
    estado = models.BooleanField(default=True)
    actividades = models.ManyToManyField(Actividad)

    def validateCompleto(self):
        if self.actividades.all():
            resultado = ResultadoAprendizaje.objects.get(pk=self.id)
            if IndicadorLogro.objects.filter(resultado=resultado, estado=True).exists():
                for indicador in IndicadorLogro.objects.filter(resultado=resultado, estado=True):
                    if indicador.validateCompleto():
                        return True
                
                return False
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
        return '{} {} {} {}'.format(self.verbo, self.contenido, self.contexto, self.proposito)
