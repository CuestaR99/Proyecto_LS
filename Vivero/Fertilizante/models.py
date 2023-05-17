from django.db import models
from Control.models import Control_Plaga

# Create your models here.
class fertilizante(models.Model):
    id_fertilizante = models.CharField(max_length=15)
    nombre_fertilizante = models.CharField(max_length=50)
    valor_fertilizante = models.DecimalField(max_digits=10, decimal_places=3)
    id_control_plaga = models.ForeignKey(Control_Plaga, on_delete=models.CASCADE)