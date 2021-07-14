from re import S
from django.conf.urls import url
from django.core.checks import messages
from django.db.models.aggregates import Avg
from django.http import Http404, JsonResponse
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from .models import Producto, Categoria, Comment, Contatecno
from cuenta.models import PerfilUsuario
from .forms import CategoriaForm, CommentForm, ProductForm, ContactoForm
from django.contrib.auth.models import User

# Create your views here.
def Index(request):
    template_name= "tienda/index.html"
    productos=Producto.objects.all()
    context={
        'productos': productos
    }
    return render(request, template_name, context)
def Detalle_categoria(request, categoria_id):
    template_name= "tienda/detalle_categoria.html"
    categoria = get_object_or_404(Categoria, id=categoria_id)
    producto = Producto.objects.filter(categoria=categoria)
    context = {
        'categoria':categoria,
        'productos': producto
    }
    return render(request,template_name, context )
#def Lista_categoria(request, category_slug=None):
#    category = get_object_or_404(Categoria, id=category_slug)
#    products = Producto.products.filter(category=category)
#    return render(request, 'store/category.html', {'category': category, 'products': products})


def Producto_detail(request, id):
    producto = get_object_or_404(Producto, id=id)
    response_data = {}
    
    reviewse = Comment.objects.filter(producto=producto)
    print(reviewse)
    answers_list = list(reviewse)
    print(answers_list)
    reviews = Comment.objects.filter(producto=producto).select_related('user')
    perfo = PerfilUsuario.objects.all().select_related('usuario')

    for b in reviewse:
           print(b.producto, b.user.profile.avatar)
    perfil = PerfilUsuario.objects.filter(usuario=b.user.id)
       
       
    review_avg = reviewse.aggregate(Avg('ranking'))
    review_one = Comment.objects.filter(ranking="1", producto=producto)
    review_two = Comment.objects.filter(ranking="2", producto=producto)
    review_three = Comment.objects.filter(ranking="3", producto=producto)
    review_four = Comment.objects.filter(ranking="4", producto=producto)
    review_five = Comment.objects.filter(ranking="5", producto=producto)
    context = {
        'producto': producto,
        'review':reviewse,
        'review_con':review_avg,
        'review_one':review_one,
        'review_two':review_two,
        'review_three':review_three,
        'review_four':review_four,
        'review_five':review_five
        
	}
    if request.method == 'POST' and request.user.is_authenticated:
        contenido = request.POST.get('contenido')
        ranking = request.POST.get('ranking')
        response_data['contenido'] = contenido
        response_data['ranking'] = ranking
        review = Comment.objects.create(producto=producto, user=request.user, contenido=contenido, ranking=ranking)
        return JsonResponse(response_data)
    else:
        review = CommentForm()


    return render(request, 'tienda/detalle.html', context)
def Contactenos(request):
    url = request.META.get('HTTP_REFERER')
    template_name= "tienda/contactenos.html"
    contacto = ContactoForm()
    if request.method == 'POST':
        contacto = ContactoForm(request.POST, request.FILES)
        if contacto.is_valid():
            contacto.save()
        return HttpResponseRedirect(url)
    context={
         'form':contacto,
    }  
    return render(request,template_name,context )
def Categoria_new(request):
    url = request.META.get('HTTP_REFERER')
    template_name= "tienda/categoria_new.html"
    categorias = Categoria.objects.all()
    categoria = CategoriaForm()
    if request.method == 'POST':
        categoria = CategoriaForm(request.POST, request.FILES)
        if categoria.is_valid():
            data = Categoria()
            data.nombre = categoria.cleaned_data['nombre']
            data.image = categoria.cleaned_data['image']
            data.save()
        return HttpResponseRedirect(url)
    context={
         'form':categoria,
        'categoria':categorias
    }  
    return render(request,template_name,context )
def Producto_new(request):
    messages={}
    producto = ProductForm(request.POST, request.FILES)
    if producto.is_valid():
        producto.save()

        producto = ProductForm
    else:
        messages = 'error'
        return render(request,'tienda/crear_producto.html',{'form': producto, 'err':messages})
    return redirect("tienda:tienda_home")
def Crear_producto(request):
    form = ProductForm()
    return render(request,'tienda/crear_producto.html',{'form': form})

def Agregar_comentario(request, id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            data = Comment()
            data.contenido = form.cleaned_data['contenido']
            #data.ranking = form.cleaned_data['ranking']
            data.producto = id
            data.ranking = 1
            current_user = request.user
            data.user = 1
            data.save()
            messages.success(request, "Su Review Su Enviada")
            return HttpResponseRedirect(url)
    return HttpResponseRedirect(url)