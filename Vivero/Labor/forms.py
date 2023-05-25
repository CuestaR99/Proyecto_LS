from django import forms

class crear_labor(forms.Form):
    fecha_labor = forms.DateField(label="Fecha de labor")
    tipo_labor = forms.CharField(label="Tipo de labor", max_length=150)
    descripcion_labor = forms.CharField(label="Descripcion de labor", max_length=200)