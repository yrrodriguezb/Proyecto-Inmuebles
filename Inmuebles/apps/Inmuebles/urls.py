from django.conf.urls import url

from .views import (
    index,
    search,
    InmueblesListView,
    InmuebleTipoListView,
    InmuebleTipoCreateView
)

app_name = 'Inmuebles'

urlpatterns = [
    url(r'^$', InmueblesListView.as_view(), name='inmuebles-listar'),
    url(r'^agregar/', InmuebleTipoCreateView.as_view(), name='tipo-inmuebles-agregar'),
]
