from django.db import models
from tienda.models import Producto
from django.contrib.auth.models import User
# Create your models here..
class Orden(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='order_user')
    direccion1 = models.CharField(max_length=250)
    direccion2 = models.CharField(max_length=250)
    ciudad = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    codigo_postal = models.CharField(max_length=20)
    total_pagado = models.DecimalField(max_digits=10, decimal_places=3)
    estado_facturacion = models.BooleanField(default=False)
    orden_pedido = models.CharField(max_length=200)
    creado = models.DateField(auto_now_add=True)
    actualizado = models.DateField(auto_now=True)
    class Meta:
        ordering = ['creado']

    def __str__(self):
        return str(self.creado)

class OrdenArticulo(models.Model):
    orden = models.ForeignKey(Orden, related_name='articulo', on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, related_name='orden_articulo', on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=10, decimal_places=3)
    cantidad = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

