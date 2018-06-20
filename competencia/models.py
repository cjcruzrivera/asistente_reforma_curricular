# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from curso.models import Curso

# Create your models here.

class Competencia(models.Model):
    descripcion = models.CharField(max_length=250)
    curso = models.ForeignKey(Curso)
    estado = models.BooleanField(default=True)

    def delete(self):
        if self.estado:
            self.estado = False
            self.save()
            return True
        else:
            return False

    def __unicode__(self):
        return '{}'.format(self.descripcion)