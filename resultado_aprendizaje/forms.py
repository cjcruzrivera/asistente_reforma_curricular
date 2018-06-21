# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django import forms
from .models import ResultadoAprendizaje


class ResultadoAprendizajeForm(forms.ModelForm):

    class Meta:
        model = ResultadoAprendizaje
        fields = [
            'verbo',
            'contenido',
            'contexto',
            'proposito',
        ]
        labels = {
            'verbo': 'Verbo',
            'contenido': 'Contenido',
            'contexto': 'Contexto o condición',
            'proposito': 'Proposito o finalidad',
        }
        widgets = {
            'verbo': forms.Select(attrs={'class': 'form-control', 'id': 'verbo_form'}),
            'contenido': forms.TextInput(attrs={'class': 'letras form-control', 'id': 'contenido_form', 'placeholder': 'Tema o herramienta sobre el que se trabaja'}),
            'contexto': forms.TextInput(attrs={'class': 'letras form-control', 'id': 'contexto_form', 'placeholder': 'Se espera que esa habilidad/destreza/conocimiento/actitud se aplique o transfiera'}),
            'proposito': forms.TextInput(attrs={'class': 'letras form-control', 'id': 'proposito_form', 'placeholder': 'Generalmente empieza con “a fin de” o “con el proposito de” o “con la finalidad de” o “para”'}),
        }
