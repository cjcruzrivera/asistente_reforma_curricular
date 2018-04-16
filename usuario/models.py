# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Usuario(models.Model):
    username = models.CharField(max_length=20)
    nombre = models.CharField(max_length=60)
    apellidos = models.CharField(max_length=60)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    roles = models.ManyToManyField('self', symmetrical=False, blank=True, through='User_Rol' , related_name='user_roles')
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

class Semestre(models.Model):
    nombre = models.CharField(max_length=10)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
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

class User_Rol(models.Model):
    usuario = models.ForeignKey(Usuario)
    rol = models.ForeignKey(Rol)
    semestre = models.ForeignKey(Semestre)
    estado = models.BooleanField(default=True)

    def delete(self):
        if self.estado:
            self.estado = False
            self.save()
            return True
        else:
            return False

    def __unicode__(self):
        return '{} {} {} {} {} {}'.format(self.usuario.nombre,self.usuario.apellidos,'-', self.rol.nombre,'-', self.semestre.nombre)