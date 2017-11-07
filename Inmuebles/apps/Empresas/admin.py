# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Empresa


class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('id', 'EmpNombre', 'EmpPaginaWeb',)
    list_display_links = ('id',)
    ordering = ('EmpNombre',)
    search_fields = ['EmpNombre',]

admin.site.register(Empresa, EmpresaAdmin)
