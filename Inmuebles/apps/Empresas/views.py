# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import ListView
from django.db.models import Q
from .models import Empresa


class EmpresasListView(ListView):
    model = Empresa
    template_name = 'Empresas/EListar.html'

    def get_queryset(self):
        query = self.request.GET.get('q', '')
        if query:
            qset = (
                Q(EmpNombre__icontains=query)
            )
            results = Empresa.objects.filter(qset).distinct()
        else:
            results = Empresa.objects.all()
        return results

    def get_context_data(self, **kwargs):
        context = super(EmpresasListView, self).get_context_data(**kwargs)
        context['params'] = { 'query' : self.request.GET.get('q', '') }
        return context
