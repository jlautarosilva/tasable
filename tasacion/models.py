from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.query_utils import RegisterLookupMixin
from address.models import AddressField

class Propiedad(models.Model):
    direccion = AddressField()
    propietario = models.CharField(max_length=200)

class Tasacion(models.Model):
    fecha = models.DateTimeField()
    tazador = models.CharField(max_length=200)
    tipoZona = models.CharField(max_length=200)
    usoPredominante = models.CharField(max_length=200)
    tipoAltura = models.IntegerField()
    propiedad = models.ForeignKey(Propiedad, on_delete=CASCADE, null=True)

