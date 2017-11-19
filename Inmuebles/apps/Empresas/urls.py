from django.conf.urls import url

from .views import EmpresasListView

app_name = 'Empresas'

urlpatterns = [
    url(r'^$', EmpresasListView.as_view(), name='empresa-listar'),
]
