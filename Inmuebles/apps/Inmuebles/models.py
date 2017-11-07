# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class InmuebleTipo(models.Model):
    ITDescripcion = models.CharField(max_length=100, verbose_name='Descripción')
    ITDescripcion_Corta = models.CharField(max_length=20, null=True, blank=True, verbose_name='Descripción Corta')

    def __str__(self):
        return self.ITDescripcion

    def getDescripcion(self):
        return self.ITDescripcion_Corta + " - " + self.ITDescripcion


class Inmueble(models.Model):
    IDescripcion = models.CharField(max_length=100, verbose_name='Descripción')
    IDireccion = models.CharField(max_length=100, verbose_name='Dirección')
    IMetros = models.IntegerField(verbose_name='Metros')
    ITipo = models.ForeignKey(InmuebleTipo, verbose_name='Tipo de Inmueble')

    def __str__(self):
        return self.IDescripcion
