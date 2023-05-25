from django import forms

class crear_fertilizante(forms.Form):
    id_fertilizante = forms.CharField(label="Referencia Fertilizante", max_length=15)
    nombre_fertilizante = forms.CharField(label="Nombre Fertilizante", max_length=50)
    valor_fertilizante = forms.DecimalField(label="Valor Fertilizante", max_digits=10, decimal_places=3)

