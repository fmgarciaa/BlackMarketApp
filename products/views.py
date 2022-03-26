from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Product, Category, Unit

class ProductList(ListView):
    model=Product



    

