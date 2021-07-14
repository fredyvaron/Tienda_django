from django.contrib import admin
from .models import Producto, Categoria, Comment, Contatecno
# Register your models here.
admin.site.register(Producto)
admin.site.register(Categoria)
admin.site.register(Comment)
admin.site.register(Contatecno)