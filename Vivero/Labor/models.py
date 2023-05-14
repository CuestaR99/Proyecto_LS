from django.db import models

# Create your models here.
class labor(models.Model):
    fecha_labor = models.DateField()
    tipo_labor = models.CharField(max_length=150)
    descripcion_labor = models.CharField(max_length=200)