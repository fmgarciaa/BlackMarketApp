from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Order, OrderItem
from products.models import Product
from cart.cart import Cart
from customers.models import Customers
import datetime

from django.urls import reverse
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

class OrderList(ListView):
    model=Order

class OrderCreate(SuccessMessageMixin, CreateView):
    model = Order
    form = Order
    fields = ('owner', 'date',  'status', 'pay_method', 'bank')
    success_message="Order created succesfully"

    def get_contetx_data(self, **kwargs):
        context = super().get_context_data()
        #luego agregas al contexto lo que desees que vaya a la otra pagina o se use en esta.
        context['id'] = self.object.id
        return context

    def get_success_url(self):
        return reverse ('order:list')
    
    def save_order(request, context):
        cart=Cart(request)
        order_id=context
        for item in cart:
            OrderItem.objects.create(
             order=order_id,
            product=item['name'],
            quantity=item['quantity'],
            price=item['price'],
        )


class OrderItemCreate(SuccessMessageMixin, CreateView):
    model = OrderItem
    form = OrderItem
    fields = ('order', 'product', 'quantity')
    success_message="Items add to order succesfully!!"

    def get_success_url(self):
        return reverse('order:list')

class OrderDetail(DetailView):
    model=Order

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['genres'] = Order.objects.all()
        context['filter'] = OrderFilter(self.request.GET, queryset=Order.objects.all())
        return context

class OrderDelete(SuccessMessageMixin, DeleteView):
    model=Order
    form=Order
    fields='__all__'

    def get_success_url(self):
        success_message='the order has been successfully deleted'
        messages.success(self.request, (success_message))
        return reverse('order:list')

class OrderUpdate(SuccessMessageMixin, UpdateView):
    model=Order
    form=Order
    fields=()
    success_message='Update Order successfully!'

    def get_success_url(self):
        return reverse('order:list')

class OrderItem(ListView):
    model=Product


def save_order(request, pk):
    cart=Cart(request)
    order_id=pk
    for item in cart:
        OrderItem.objects.create(
            order=order_id,
            product=item['name'],
            quantity=item['quantity'],
            price=item['price'],
        )
    
    return reverse('order:list')