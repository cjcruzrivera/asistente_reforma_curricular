# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from programa.models import Programa
# Create your models here.

class Tipo_Curso(models.Model):
    nombre = models.CharField(max_length=50)
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
    

class Curso(models.Model):
    nombre = models.CharField(max_length=50)
    creditos = models.IntegerField()
    programa = models.ForeignKey(Programa, null=True)
    horas_catedra = models.IntegerField()
    horas_individual = models.IntegerField()
    tipo = models.ForeignKey(Tipo_Curso, null=True)
    estado = models.BooleanField(default=True)
    prerrequisitos = models.ManyToManyField('self',blank=True)

    def delete(self):
        if self.estado:
            self.estado = False
            self.save()
            return True
        else:
            return False

    def __unicode__(self):
        return '{}'.format(self.nombre)