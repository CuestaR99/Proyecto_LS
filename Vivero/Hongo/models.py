from django.db import models
from Control.models import Control_Plaga

# Create your models here.
class hongo(models.Model):
    id_hongo = models.CharField(max_length=20)
    nombre_hongo = models.CharField(max_length=50)
    tipo_hongo = models.CharField(max_length=50)
    id_control_plagaa = models.ForeignKey(Control_Plaga, on_delete=models.CASCADE)