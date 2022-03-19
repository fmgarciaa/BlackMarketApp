from django.db import models
from django.utils import timezone

from customers.models import Customers
from products.models import Product

STATUS_CHOICES = (
    ("1","Peid"),
    ("2", "Pending"),
)

PAY_CHOICES = (
    ("C","Cash"),
    ("T","Transfer"),
)

BANK_CHOICES = (
    ("1","BCP"),
    ("2","BBVA"),
    ("3","SCOTIABANK"),
    ("4","INTERBANK"),
    ("5","BANCO DE LA NACION"),
    ("6", "None")
)

class Order(models.Model):
    owner = models.ForeignKey(Customers, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=13, choices=STATUS_CHOICES, default="Pending")
    pay_method = models.CharField(max_length=12, choices=PAY_CHOICES)
    bank = models.CharField(max_length=27, choices=BANK_CHOICES, default="6")
    total_pay = models.DecimalField(decimal_places=2, max_digits=5, default=0)
    register_date =models.DateTimeField()

    def save(self, *args, **kwargs):
        self.register_date = timezone.now()
        super(Order, self).save(*args, **kwargs)

    class Meta:
        ordering = ('-id',)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="orderItems")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="orderItem")
    quantity = models.PositiveSmallIntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=7)
    register_date =models.DateTimeField()

    def save(self, *args, **kwargs):
        self.register_date = timezone.now()
        super(OrderItem, self).save(*args, **kwargs)



