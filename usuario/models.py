# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Usuario(models.Model):
    username = models.CharField(max_length=20)
    nombre = models.CharField(max_length=60)
    apellidos = models.CharField(max_length=60)
    rol = models.CharField(max_length=60)