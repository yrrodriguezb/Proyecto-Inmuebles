# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from  django.contrib.auth.forms import UserCreationForm


class RegistroUsuarioForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
        ]
        labels = {
            'username': 'Nombre de Usuario',
            'first_name': 'Nombre',
            'last_name': 'Apellidos',
            'email': 'Correo electronico',
        }
