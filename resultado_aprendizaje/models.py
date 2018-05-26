# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from competencia.models import Competencia
# Create your models here.

class ResultadoAprendizaje(models.Model):
    descripcion = models.CharField(max_length=250)
    competencia = models.ForeignKey(Competencia)