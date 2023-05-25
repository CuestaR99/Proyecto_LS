from django import forms

class crear_productor(forms.Form):
    cedula = forms.CharField(label="Cedula", max_length=15)
    nombre = forms.CharField(label="Nombre", max_length=50)
    apellido = forms.CharField(label="Apellido", max_length=50)
    telefono = forms.CharField(label="Telefono", max_length=15)
    correo = forms.EmailField(label="Correo Electronico")


