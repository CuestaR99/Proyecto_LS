from django import forms

class crear_vivero(forms.Form):
    Codigo_vivero = forms.CharField(label="Codigo Vivero", max_length=50)
    Nombre_vivero = forms.CharField(label="Nombre Vivero", max_length=100)
    Tipo_cultivo = forms.CharField(label="Tipo de Cultipo", max_length=150)

class crear_ubicacion(forms.Form):
    Departemento = forms.CharField(label="Departamento", max_length=150)
    Municipio = forms.CharField(label="Muncipio", max_length=150)
    Vereda = forms.CharField(label="Vereda", max_length=150)