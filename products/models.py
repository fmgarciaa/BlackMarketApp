from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=170, unique=True)
    type = models.CharField(max_length=170)
    unity = models.CharField(max_length=170)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    
