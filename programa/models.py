# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from escuela.models import Escuela
from usuario.models import Usuario    

# Create your models here.

class Programa(models.Model):
    nombre = models.CharField(max_length=50,unique=True)
    semestres = models.IntegerField()
    creditos = models.IntegerField()
    estado = models.BooleanField(default=True)
    cod_escuela = models.ForeignKey(Escuela)
    dir_programa = models.OneToOneField(Usuario,blank=True, null=True)

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
