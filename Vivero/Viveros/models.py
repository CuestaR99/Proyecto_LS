from django.db import models

# Create your models here.
class vivero(models.Model):
    Codigo_vivero = models.CharField(max_length=50)
    Nombre_vivero = models.CharField(max_length=100)
    Tipo_cultivo = models.CharField(max_length=150)

class ubicacion(models.Model):
    Departemento = models.CharField(max_length=150)
    Municipio = models.CharField(max_length=150)
    Vereda = models.CharField(max_length=150)