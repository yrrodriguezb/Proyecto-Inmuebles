# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from .models import InmuebleTipo


class InmuebleTipoTestCase(TestCase):

    def setUp(self):
        InmuebleTipo.objects.create(ITDescripcion='Casas')

    def test_InmTipo_have_ITDescripcion(self):
         InmTipo = InmuebleTipo.objects.get(ITDescripcion='Casas')

         self.assertEqual(InmTipo.ITDescripcion, "Casaaas", msg=None)
