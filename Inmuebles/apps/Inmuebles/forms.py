from django import forms


class InmuebleTipoForm(forms.Form):
    ITDescripcion = forms.CharField(label='Descripcion', max_length=100)
    ITDescripcion_corta = forms.CharField(label='Descripcion Corta', max_length=20, empty_value='')
