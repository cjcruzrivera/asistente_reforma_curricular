# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Escuela(models.Model):
    nombre_largo = models.CharField(max_length=50, unique=True)
    nombre_corto = models.CharField(max_length=10, unique=True)
    estado = models.BooleanField(default=True)

    def delete(self):
        if self.estado:
            self.estado = False
            self.save()
            return True
        else:
            return False

    def __unicode__(self):
        return '{} {} {}'.format(self.nombre_corto, ' - ' , self.nombre_largo)
