from django.contrib import admin

# Register your models here.
from .models import Tasacion, Propiedad
admin.site.register(Propiedad)
admin.site.register(Tasacion)