# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from curso.models import Curso

# Create your models here.

class Competencia(models.Model):
    descripcion = models.CharField(max_length=250)
    curso = models.ForeignKey(Curso)