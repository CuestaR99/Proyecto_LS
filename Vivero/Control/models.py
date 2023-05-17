from django.db import models
from Labor.models import labor

# Create your models here.
class control(models.Model):
    tipo_control = models.CharField(max_length=100)
    nombre_control = models.CharField(max_length=100)
    id_labor = models.ForeignKey(labor, on_delete=models.CASCADE)

class Control_Plaga(models.Model):
    periodo_carencia = models.DateField()
    registro_ICA = models.CharField(max_length=50)
    frecuencia_aplicacion = models.DateField()
    id_control = models.ForeignKey(control, on_delete=models.CASCADE)
    