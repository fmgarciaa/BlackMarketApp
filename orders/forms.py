from django import forms
from .models import Order
from cart.context_processor import data_cart

class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = [
            'customer',
            'date',
            'pay_method',
            'bank',
            'total_pay',
        ]

   
    