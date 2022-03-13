from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Product

from django.urls import reverse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django import forms

class ProductList(ListView):
    model=Product


class ProductCreate(SuccessMessageMixin, CreateView):
    model=Product
    form= Product
    fields = ('name', 'description', 'type', 'unity', 'price')
    success_message= 'Product created successfully!'

    def get_success_url(self):        
        return reverse('product:list') 

class ProductDetail(DetailView):
    model=Product

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['genres'] = Product.objects.all()
        context['filter'] = ProductFilter(self.request.GET, queryset=Product.objects.all())
        return context


class ProductUpdate(SuccessMessageMixin, UpdateView):
    model = Product
    form = Product
    fields=('name', 'description', 'type', 'unity', 'price') 
    success_message = 'Updated product successfully!'

    def get_success_url(self):
        return reverse('product:list')

class ProductDelete(SuccessMessageMixin, DeleteView):
    model=Product
    form=Product
    fields='__all__'

    def get_success_url(self):
        success_message='Delet product successfully!'
        messages.success(self.request, (success_message))
        return reverse('product:list')
    

