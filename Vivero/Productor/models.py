from django.db import models

# Create your models here.
class productor(models.Model):
    Cedula = models.CharField(max_length=15)
    Nombre = models.CharField(max_length=50)
    Apellido = models.CharField(max_length=50)
    Telefono = models.CharField(max_length=15)
    Correo = models.EmailField()
