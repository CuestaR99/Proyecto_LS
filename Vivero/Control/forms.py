from django import forms


class control_viveros(forms.Form):
    tipo_control = forms.CharField(label="Tipo de control", max_length=100)
    nombre_control = forms.CharField(label="Nombre del control", max_length=100)    

class control_plaga(forms.Form):
    periodo_carencia = forms.DateField(label="Periodo de carencia")
    registro_ICA = forms.CharField(label="Número de registro ICA", max_length=50)
    frecuencia_aplicacion = forms.IntegerField(label="Frecuencia de aplicación")

