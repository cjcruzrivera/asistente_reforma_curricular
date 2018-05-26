# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser

from django.db import models
from programa.models import Programa

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

class Usuario(AbstractUser):
    '''
    estos campos se heredan de AbastractUser
    username = models.CharField(max_length=20)
    nombre = models.CharField(max_length=60)
    apellidos = models.CharField(max_length=60)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    '''
    rol = models.ForeignKey(Rol, null=True)
    escuela = models.ForeignKey(Programa, null=True)
    estado = models.BooleanField(default=True)

    def delete(self):
        if self.estado:
            self.estado = False
            self.save()
            return True
        else:
            return False

    def __unicode__(self):
        return '{} {}'.format(self.first_name, self.last_name)

