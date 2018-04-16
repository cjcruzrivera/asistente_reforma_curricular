# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from escuela.models import Escuela

# Create your models here

class Rol(models.Model):
    nombre = models.CharField(max_length=20)
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

class Usuario(models.Model):
    username = models.CharField(max_length=20)
    nombre = models.CharField(max_length=60)
    apellidos = models.CharField(max_length=60)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    roles = models.ManyToManyField(Rol)
    escuela = models.ForeignKey(Escuela, null=True)
    estado = models.BooleanField(default=True)

    def delete(self):
        if self.estado:
            self.estado = False
            self.save()
            return True
        else:
            return False

    def __unicode__(self):
        return '{} {}'.format(self.nombre, self.apellidos)

