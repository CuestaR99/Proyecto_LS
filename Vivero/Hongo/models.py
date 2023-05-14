from django.db import models

# Create your models here.
class hongo(models.Model):
    id_hongo = models.CharField(max_length=20)
    nombre_hongo = models.CharField(max_length=50)
    tipo_hongo = models.CharField(max_length=50)