from itertools import count, product
from django.shortcuts import render
from products.models import Product
from .forms import OrderForm
from orders.models import OrderItem, Order
from cart.context_processor import data_cart
from cart.cart import Cart
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView


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
            if not key == 'is_modify' and not key == 'id_update':
                product = Product.objects.get(pk=key)
                value = cart[key]
                OrderItem.objects.create(order=order, product=product,
                    quantity=(value['quantity']), price=(value['price']),
                )

        basket = Cart(request)
        basket.clean_cart()
        messages.add_message(request, messages.INFO, 'Order was created succesfuly!!')
        return HttpResponseRedirect(reverse('order:create')) 

    
    context['form'] = form
    return render(request, 'orders/checkout.html', context)

def all_orders(request):
    orders = Order.objects.filter(is_active=True)
    return render(request, 'orders/list_orders.html', {'orders': orders})

class OrderDelete(SuccessMessageMixin, DeleteView):
    model = Order
    form = Order
    fields='__all__'

    def get_success_url(self):
        success_message='the client has been successfully deleted'
        messages.success(self.request, (success_message))
        return reverse('order:list')

class UpdateOrder(SuccessMessageMixin, UpdateView):
    model = Order
    form = Order
    fields=('customer', 'date', 'pay_method', 'bank', 'status', 'total_pay' )
    success_message = 'Updated order successfully!'

    def get_success_url(self):
        return reverse('order:list')

def update_items(request, id):
    cart = Cart(request)
    cart.cart['is_modify'] = True
    cart.cart['id_update'] = id
    items = OrderItem.objects.filter(order=id).values_list()
    for item in items:
        product = Product.objects.get(id=item[2])
        cart.add_item(product=product, qty=item[3])

    data = data_cart(request)
    data['total_items'] = len(items)

    return render(request, 'cart/summary.html', {'items': items})

def modify_order(request):
    cart = request.session['cart']
    data = data_cart(request)
    order_id=cart['id_update']
    Order.objects.filter(pk=order_id).update(total_pay=data['total_cart'])
    order=Order.objects.get(pk=order_id)
    OrderItem.objects.filter(order=order_id).delete()
    for key in cart:
        if not key == 'is_modify' and not key == 'id_update':
            product = Product.objects.get(pk=key)
            value = cart[key]
            OrderItem.objects.create(order=order, product=product,
            quantity=(value['quantity']), price=(value['price']),
            )

    basket = Cart(request)
    cart['is_modify'] = False
    basket.clean_cart()
    messages.add_message(request, messages.INFO, 'Order was modify succesfuly!!')
    return HttpResponseRedirect(reverse('order:list')) 

    
