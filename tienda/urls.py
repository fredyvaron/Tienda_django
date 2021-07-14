"""tiendaonline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from .views import Index, Producto_detail,  Agregar_comentario, Crear_producto, Producto_new, Categoria_new, Detalle_categoria, Contactenos

app_name = 'tienda'
urlpatterns = [
    path('', Index, name='tienda_home'),
    path('<int:id>', Producto_detail, name='producto_detail'),
    path('crearproducto/', Crear_producto, name='crear_producto'),
    path('productonew/', Producto_new, name='new_producto'),
    path('categoria/', Categoria_new, name='new_categoria'),
    path('contactenos/', Contactenos, name='contactenos'),
    path('detallecategoria/<int:categoria_id>', Detalle_categoria, name='detalle_categoria'),
    path('addcoment/<int:id>/', Agregar_comentario, name='agregar_comentario' )

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)