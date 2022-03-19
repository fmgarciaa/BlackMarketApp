from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Order, OrderItem
from products.models import Product
from .basket import Basket

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

    def get_success_url(self):
        return reverse('order:addItem')

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

def add_product(request, product_id):
    basket = Basket(request)
    product=Product.objects.get(id=product_id)

    basket.add_item(product=product)

    return redirect('product:list')

def delete_product(request, product_id):
    basket = Basket(request)
    product=Product.objects.get(id=product_id)

    basket.delete(product=product)

    return redirect('product:list')

def remove_product(request, product_id):
    basket = Basket(request)
    product=Product.objects.get(id=product_id)

    basket.remove_item(product=product)

    return redirect('product:list')

def clean_basket(request, product_id):
    basket = Basket(request)

    basket.clean_basket()
    return redirect('product:list')