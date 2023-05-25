from django import forms

class crear_productor(forms.Form):
    Cedula = forms.CharField(label="Cedula", max_length=15)
    Nombre = forms.CharField(label="Nombre", max_length=50)
    Apellido = forms.CharField(label="Apellido", max_length=50)
    Telefono = forms.CharField(label="Telefono", max_length=15)
    Correo = forms.EmailField(label="Correo Electronico")


