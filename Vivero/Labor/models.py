from django.db import models
from Viveros.models import vivero

# Create your models here.
class labor(models.Model):
    fecha_labor = models.DateField()
    tipo_labor = models.CharField(max_length=150)
    descripcion_labor = models.CharField(max_length=200)
    id_vivero = models.ForeignKey(vivero, on_delete=models.CASCADE)