from django.db import models

# Create your models here.
class Registro(models.Model):
    nombre=models.CharField(max_length=50)
    correo=models.CharField(max_length=100)
    contraseña=models.CharField(max_length=50)