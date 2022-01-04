from django.db import models

# Create your models here.

class Tasacion(models.Model):
    tazador = models.CharField(max_length=200)
    fecha = models.DateTimeField('date published')
    tipoZona = models.CharField(max_length=200)
    usoPredominante = models.CharField(max_length=200)
    tipoAltura = models.IntegerField()