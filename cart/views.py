from django.shortcuts import render
from products.models import Product
from django.shortcuts import redirect
from .cart import Cart


def add_product(request, product_id):
    cart = Cart(request)
    product=Product.objects.get(id=product_id)

    cart.add_item(product=product)

    return redirect('order:orderitem')

def delete_product(request, product_id):
    cart = Cart(request)
    product=Product.objects.get(id=product_id)

    cart.delete(product=product)

    return redirect('cart:home')

def remove_product(request, product_id):
    cart = Cart(request)
    product=Product.objects.get(id=product_id)

    cart.remove_item(product=product)

    return redirect('cart:home')

def clean_cart(request, product_id):
    cart = Cart(request)

    cart.clean_cart()
    return redirect('cart:home')

def sum_product(request, product_id):
    cart = Cart(request)
    product=Product.objects.get(id=product_id)

    cart.add_item(product=product)

    return redirect('cart:home')
