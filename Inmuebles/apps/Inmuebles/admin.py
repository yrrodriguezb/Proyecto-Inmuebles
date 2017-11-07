# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Inmueble, InmuebleTipo


class InmuebleAdmin(admin.ModelAdmin):
    fields = ['IDescripcion', 'IDireccion', 'IMetros', 'ITipo']
    list_display = ('id', 'IDescripcion', 'IDireccion', 'IMetros', 'ITipo', )
    ordering = ('id', 'IDescripcion',  )
    search_fields = ['IDescripcion', 'ITipo__ITDescripcion', ]


class InmuebleTipoAdmin(admin.ModelAdmin):
    list_display = ('id', 'ITDescripcion', 'ITDescripcion_Corta',)
    list_display_links = ('id',)
    list_filter = ('ITDescripcion', 'ITDescripcion_Corta',)
    ordering = ('id', 'ITDescripcion',)


admin.site.register(Inmueble, InmuebleAdmin)
admin.site.register(InmuebleTipo, InmuebleTipoAdmin)
