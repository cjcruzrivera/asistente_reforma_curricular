# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser

from django.db import models

from programa.models import Programa
# Create your models here

class Rol(models.Model):
    nombre = models.CharField(max_length=20, unique=True)
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
    escuela = models.ForeignKey('escuela.Escuela', null=True)
    estado = models.BooleanField(default=True)

    def is_dir(self):
        programas = Programa.objects.filter(estado=True)
        for programa in programas:
            if(self == programa.dir_programa):
                return True
        return False

    def delete(self):
        if self.estado:
            self.username = self.username+'_borrado'
            self.estado = False
            self.save()
            return True
        else:
            return False

    def __unicode__(self):
        return '{} {}'.format(self.first_name, self.last_name)

