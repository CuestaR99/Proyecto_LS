from django import forms

class crear_hongo(forms.Form):
    id_hongo = forms.CharField(label="Referencia hongo", max_length=20)
    nombre_hongo = forms.CharField(label="Nombre Hongo", max_length=50)
    tipo_hongo = forms.CharField(label="Tipo de hongo", max_length=50)