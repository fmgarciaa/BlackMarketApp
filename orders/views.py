from django.shortcuts import render
from products.models import Product
from .forms import OrderForm
from orders.models import OrderItem, Order
from cart.context_processor import data_cart
from cart.cart import Cart


def all_products(request):
    products= Product.objects.filter(is_active=True)
    return render(request, 'orders/index.html', {'products': products})

def checkout_order(request):
    cart = request.session['cart']
    context = {}
    data = data_cart(request)
    form = OrderForm(request.POST or None, initial={'total_pay':round(data['total_cart'],2)})
    
    if form.is_valid():
        note = form.save()
        form.save()
        order_id = note.id
        order=Order.objects.get(pk=order_id)
    
        for key in cart:
            product = Product.objects.get(pk=key)
            value = cart[key]
            OrderItem.objects.create(order=order, product=product,
                quantity=(value['quantity']), price=(value['price']),
            )

        barket = Cart(request)
        barket.clean_cart()

    
    context['form'] = form
    return render(request, 'orders/checkout.html', context)
