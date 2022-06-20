from django.shortcuts import render
from django.shortcuts import redirect

from .cart import Cart
from products.models import Product

def cart_summary(request):
    request.session['cart']
    return render(request, 'cart/summary.html')

def add_product(request, product_id):
    basket = Cart(request)
    product = Product.objects.filter(id=product_id).first()
    basket.add_item(product=product)
    return redirect("order:create")

def increase_quantity(request, product_id):
    cart = Cart(request)
    product = Product.objects.get(id=product_id)
    cart.add_item(product=product)
    return redirect("cart:cart_summary")


def delete_product(request, product_id):
    cart = Cart(request)
    product = Product.objects.get(id=product_id)
    cart.delete_item(product=product)
    return redirect("cart:cart_summary")

def remove_product(request, product_id):
    cart = Cart(request)
    product = Product.objects.get(id=product_id)
    cart.remove_item(product=product)
    return redirect("cart:cart_summary")

def clear_cart(request, product_id):
    cart = Cart(request)
    cart.clean_cart()
    return redirect("cart:cart_summary")

