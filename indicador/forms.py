# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django import forms
from .models import IndicadorLogro


class IndicadorForm(forms.ModelForm):

    class Meta:
        model = IndicadorLogro
        fields = [
            'habilidad',
            'contenido',
            'contexto',
        ]
        labels = {
            'habilidad': 'Habilidad',
            'contenido': 'Contenido',
            'contexto': 'Contexto o condición',
        }
        widgets = {
            'habilidad': forms.Select(attrs={'class': 'form-control', 'id': 'habilidad_form'}),
            'contenido': forms.TextInput(attrs={'class': 'letras form-control', 'id': 'contenido_form', 'placeholder': 'Tema o herramienta sobre el que se trabaja'}),
            'contexto': forms.TextInput(attrs={'class': 'letras form-control', 'id': 'contexto_form', 'placeholder': 'Donde se espera que esa habilidad/destreza/conocimiento/actitud se aplique o transfiera'}),
        }
