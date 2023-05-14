from django.db import models

# Create your models here.
class control(models.Model):
    tipo_control = models.CharField(max_length=100)
    nombre_control = models.CharField(max_length=100)

class Control_Plaga(models.Model):
    periodo_carencia = models.DateField()
    registro_ICA = models.CharField(max_length=50)
    frecuencia_aplicacion = models.DateField()
    