from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    image = models.ImageField(upload_to='categorias/', default='images/default.png')
    #slug = models.SlugField(max_length=255, unique=True)
    def get_absolute_url(self):
        return reverse('tienda:detalle_categoria', args=[self.id])
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    name = models.CharField(max_length=50)
    descripcion = models.TextField()
    #slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=30, decimal_places=1)
    image = models.ImageField(upload_to='products/', default='images/default.png')
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE , related_name='productos')
    creado = models.DateField(auto_now_add=True)
    actualizado = models.DateField(auto_now=True)
    class Meta:
        ordering = ['-creado']

    def get_absolute_url(self):
        return reverse('tienda:producto_detail', args=[self.id])

    def __str__(self):
        return self.name

class Comment(models.Model):

    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ranking = models.IntegerField(default=1)
    contenido = models.TextField()
    creado = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.contenido


class Contatecno(models.Model):
    nombre = models.CharField(max_length=70)
    asunto = models.CharField(max_length=100)
    correo = models.EmailField(max_length=254)
    mensaje = models.TextField()
    telefono = models.CharField(max_length=20)


    def __str__(self):
        return self.nombre