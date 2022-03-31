from django import forms
from . models import Unit, Category, Product
from django.core.exceptions import ValidationError
from django.core import validators

class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields= {'name', 'price', 'unit', 'category', 'description'}
    
    
   