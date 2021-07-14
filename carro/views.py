from django.http import JsonResponse
from django.shortcuts import render, redirect
from tienda.models import Producto
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from .carro import Carro


@login_required(login_url="/accounts/login/")
def cart_add(request, id):
    cart = Cart(request)
    product = Producto.objects.get(id=id)
    cart.add(product=product)
    return redirect("tienda:tienda_home")


@login_required(login_url="/accounts/login/")
def item_clear(request, id):
    cart = Cart(request)
    product = Producto.objects.get(id=id)
    cart.remove(product)
    return redirect("carro:cart_detail")


@login_required(login_url="/accounts/login/")
def item_increment(request, id):
    cart = Cart(request)
    product = Producto.objects.get(id=id)
    cart.add(product=product)
    return redirect("carro:cart_detail")


@login_required(login_url="/accounts/login/")
def item_decrement(request, id):
    cart = Cart(request)
    product = Producto.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("carro:cart_detail")


@login_required(login_url="/accounts/login/")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("carro:cart_detail")


@login_required(login_url="/accounts/login/")
def cart_detail(request):
    car = Carro(request)
    template_name= "carro/suma.html"
    context={
        'carros': car    
    }
    return render(request, template_name, context)

