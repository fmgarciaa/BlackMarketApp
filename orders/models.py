from django.db import models

from customers.models import Customers
from products.models import Product



class Order(models.Model):
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE)
    date = models.DateField()
    pay_method = models.CharField(max_length=255)
    bank = models.CharField(max_length=255)
    total_pay = models.DecimalField(decimal_places=2, max_digits=5, blank=True)
    status = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
   
    class Meta:
        verbose_name_plural = 'orders'
        ordering = ('-created',)

    def __str__(self):
        return str(self.pk)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=5)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'orderitems'
        ordering = ('-created',)

    

    



