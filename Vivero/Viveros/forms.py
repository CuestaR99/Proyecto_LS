from django import forms

class crear_vivero(forms.Form):
    codigo_vivero = forms.CharField(label="Codigo Vivero", max_length=50)
    nombre_vivero = forms.CharField(label="Nombre Vivero", max_length=100)
    tipo_cultivo = forms.CharField(label="Tipo de Cultipo", max_length=150)

class crear_ubicacion(forms.Form):
    departemento = forms.CharField(label="Departamento", max_length=150)
    municipio = forms.CharField(label="Muncipio", max_length=150)
    vereda = forms.CharField(label="Vereda", max_length=150)