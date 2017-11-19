# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, UpdateView, FormView, TemplateView, RedirectView

from .forms import RegistroUsuarioForm
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect


class UsuarioUpdateView(UpdateView):
    model = User
    fields = [ 'id', 'username', 'first_name', 'last_name', 'email' ]
    template_name = 'Usuario/UActualizar.html'
    success_url = reverse_lazy('Usuarios:usuario-actualizar')


    def get_object(self):
        """myDict = {}
        for key in self.request.POST.iterkeys():
            myDict[key] = self.request.POST.getlist(key)
        print myDict['username']"""

        return get_object_or_404(User, pk=self.request.user.pk)


class UsuarioCreateView(CreateView):
    model = User
    template_name = 'Usuario/UCrear.html'
    form_class = RegistroUsuarioForm
    success_url = reverse_lazy('Usuarios:usuario-login')


class LoginView(FormView):
    form_class = AuthenticationForm
    template_name = "Usuario/ULogin.html"
    success_url =  reverse_lazy("Inmuebles:inmuebles-listar")

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(LoginView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(LoginView, self).form_valid(form)


class LogoutView(RedirectView):
    pattern_name = 'Usuarios:usuario-login'

    def get_redirect_url(self, *args, **kwargs):
        if self.request.user.is_authenticated():
            logout(self.request)
        return super(LogoutView, self).get_redirect_url(*args, **kwargs)
