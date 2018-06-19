# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from programa.models import Programa
from usuario.models import Usuario
# Create your models here.

class TipoCurso(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    estado = models.BooleanField(default=True)

    def delete(self):
        if self.estado:
            self.nombre = self.nombre+'_borrado'            
            self.estado = False
            self.save()
            return True
        else:
            return False

    def __unicode__(self):
        return '{}'.format(self.nombre)


class Curso(models.Model):
    nombre = models.CharField(max_length=50)
    codigo = models.CharField(max_length=25, unique=True)
    creditos = models.IntegerField()
    programa = models.ForeignKey(Programa, blank=True, null=True)
    horas_catedra = models.IntegerField()
    horas_individual = models.IntegerField()
    tipo = models.ForeignKey(TipoCurso)
    estado = models.BooleanField(default=True)
    prerrequisitos = models.ManyToManyField('self', blank=True)
    docente_encargado = models.ForeignKey(Usuario, null=True, blank=True)
    semestre = models.IntegerField()
    validable = models.BooleanField()
    habilitable = models.BooleanField()

    def delete(self):
        if self.estado:
            self.codigo = self.codigo+'_borrado'            
            self.estado = False
            self.save()
            return True
        else:
            return False

    def __unicode__(self):
        return '{}'.format(self.nombre)
