from django.contrib import admin
from .models import Orden, OrdenArticulo
# Register your models here.
admin.site.register(Orden)
admin.site.register(OrdenArticulo)