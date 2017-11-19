from django.conf.urls import url
from .views import LoginView, LogoutView, UsuarioCreateView, UsuarioUpdateView


urlpatterns = [
    url(r'^actualizar', UsuarioUpdateView.as_view(), name='usuario-actualizar'),
    url(r'^registrar', UsuarioCreateView.as_view(), name='usuario-registrar'),
    url(r'^login', LoginView.as_view(), name='usuario-login'),
    url(r'^logout', LogoutView.as_view(), name='usuario-logout'),
]
