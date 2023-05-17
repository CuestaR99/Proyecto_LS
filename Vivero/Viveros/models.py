from django.db import models
from Productor.models import productor
# Create your models here.
class vivero(models.Model):
    Codigo_vivero = models.CharField(max_length=50)
    Nombre_vivero = models.CharField(max_length=100)
    Tipo_cultivo = models.CharField(max_length=150)
    id_productor = models.ForeignKey(productor, on_delete=models.CASCADE)

class ubicacion(models.Model):
    Departemento = models.CharField(max_length=150)
    Municipio = models.CharField(max_length=150)
    Vereda = models.CharField(max_length=150)
    id_vivero = models.ForeignKey(vivero, on_delete=models.CASCADE)