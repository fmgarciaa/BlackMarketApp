from secrets import choice
from django import forms
from .models import Order
from cart.context_processor import data_cart
from customers.models import Customers

class OrderForm(forms.ModelForm):
    PAY_METHOD_CHOICES = [
        ('Cash', 'Cash'),
        ('Transfer', 'Transfer'),
    ]

    BANK_CHOICES = [
        ('None', 'None'),
        ('BCP', 'BCP'),
        ('IBK', 'INTERBANK'),
        ('BBVA', 'BBVA'),
        ('SCOTIABANK', 'SCOTIABANK'),
        ('BN', 'Banco de la Nacion'),
    ]

    customer = forms.ModelChoiceField(queryset=Customers.objects.all(),)
    date = forms.DateField()
    pay_method = forms.CharField(max_length=27, widget=forms.Select(choices=PAY_METHOD_CHOICES))
    bank = forms.CharField(max_length=27, widget=forms.Select(choices=BANK_CHOICES))
    total_pay = forms.DecimalField(decimal_places=2, max_digits=7)


    class Meta:
        model = Order
        fields = [
            'customer',
            'date',
            'pay_method',
            'bank',
            'total_pay',
        ]

   
    