# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Empresa(models.Model):
    EmpNombre = models.CharField(max_length=255, verbose_name="Nombre o razón social")
    EmpDireccion = models.CharField(max_length=255, verbose_name="Dirección")
    EmpNit = models.CharField(max_length=100, verbose_name="Nit")
    EmpTelefono = models.CharField(max_length=100, verbose_name="Teléfono")
    EmpCelular = models.CharField(max_length=100, null=True, blank=True, verbose_name="Celular")
    EmpEmail = models.EmailField(max_length=255, null=True, blank=True, verbose_name="Correo Electronico")
    EmpPaginaWeb = models.URLField(verbose_name="URL")
    EmpLogo = models.ImageField(upload_to="Logos/Empresas", null=True, blank=True, verbose_name="Logo")

    def __str__(self):
        return self.EmpNombre
