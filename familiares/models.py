from datetime import date
from django.db import models
from django.forms import CharField,IntegerField,DateField

# Create your models here.
class registro_familiar(models.Model):
    nombre = models.CharField(max_length=60)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField()
    