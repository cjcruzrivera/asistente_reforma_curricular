# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from escuela.models import Escuela

# Create your models here.

class Programa(models.Model):
    nombre = models.CharField(max_length=50)
    semestres = models.IntegerField()
    creditos = models.IntegerField()
    estado = models.BooleanField(default=True)
    escuela = models.ForeignKey(Escuela, null=True)

    def delete(self):
        if self.estado:
            self.estado = False
            self.save()
            return True
        else:
            return False

    def __unicode__(self):
        return '{}'.format(self.nombre)
