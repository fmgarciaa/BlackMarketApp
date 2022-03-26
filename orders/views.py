from django.shortcuts import render
from products.models import Product

def all_products(request):
    products= Product.objects.filter(is_active=True)
    return render(request, 'orders/index.html', {'products': products})