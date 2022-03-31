from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import IntegrityError
from django.http import HttpResponse
from django.contrib import messages
from .forms import ProductForm

from .models import Product, Category, Unit

class ProductList(ListView):
    model=Product

class ProductDelete(SuccessMessageMixin, DeleteView):
    model=Product
    form=Product
    fields='__all__'

    def get_success_url(self):
        success_message='Delet product successfully!'
        messages.success(self.request, (success_message))
        return reverse('product:index')

class ProductUpdate(SuccessMessageMixin, UpdateView):
    model = Product
    form = Product
    fields=('name', 'price', 'unit', 'category', 'description') 
    success_message = 'Updated product successfully!'

    def get_success_url(self):
        return reverse('product:index')

class ProductCreate(SuccessMessageMixin, CreateView, LoginRequiredMixin):
    model=Product
    form=Product
    fields = ('name', 'price', 'unit', 'category', 'description')
    success_message= 'Product created successfully!'

    def get_success_url(self):        
        return reverse('product:index') 
    
    def form_valid(self, form):
        object = form.save(commit=False)
        object.create_by = self.request.user
        object.save()
        return super(ProductCreate, self).form_valid(form)
        
    
            
        
    


    

