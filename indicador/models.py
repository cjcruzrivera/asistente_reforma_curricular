# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from actividad.models import Actividad
from competencia.models import Competencia
from resultado_aprendizaje.models import ResultadoAprendizaje

# Create your models here.

class IndicadorLogro(models.Model):
    habilidades = (('Distingue','Distingue'),('Analiza', 'Analiza'), ('Reconoce','Reconoce'), ('Resuelve','Resuelve'), ('Genera','Genera'), ('Asimila','Asimila'),('Retroalimenta', 'Retroalimenta'))
    habilidad = models.CharField(max_length=250, choices=habilidades)
    contenido = models.CharField(max_length=250)
    contexto = models.CharField(max_length=250)
    resultado = models.ForeignKey('resultado_aprendizaje.ResultadoAprendizaje')
    estado = models.BooleanField(default=True)
    actividades = models.ManyToManyField(Actividad,through='Evaluaciones', symmetrical=False)

    def validateCompleto(self):
        if self.actividades.all():
            return True
        else:
            return False

    def get_curso(self):
        return self.resultado.competencia.curso

    def max_Porcentaje(self):
        porcentaje = 100
        
        curso = self.get_curso()
        competencias = Competencia.objects.filter(curso=curso)
        resultados = ResultadoAprendizaje.objects.filter(competencia__in=competencias)
        indicadores = IndicadorLogro.objects.filter(resultado__in=resultados)
        evaluaciones = Evaluaciones.objects.fliter(indicador__in=indicadores)



        return porcentaje

    def delete(self):
        if self.estado:
            self.estado = False
            self.save()
            return True
        else:
            return False

    def __unicode__(self):
        return '{}'.format(self.descripcion)


class Evaluaciones(models.Model):
    indicador = models.ForeignKey(IndicadorLogro)
    actividad = models.ForeignKey(Actividad)
    porcentaje = models.FloatField()
    estado = models.BooleanField(default=True)

    def delete(self):
        if self.estado:
            self.estado = False
            self.save()
            return True
        else:
            return False
    
    
