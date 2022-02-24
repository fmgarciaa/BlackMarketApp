import imp
from django.db import models
from django.utils import timezone


class Product(models.Model):
    name = models.CharField(max_length=170, unique=True, blank=False)
    description = models.TextField()
    type = models.CharField(max_length=170)
    unity = models.CharField(max_length=170)
    price = models.PositiveBigIntegerField(default=0)
    register_date = models.DateTimeField()

    def __str__(self) -> str:
        return self.name
    
    def save(self, *args, **kwargs):
        self.register_date = timezone.now()
        super(Product, self).save(*args, **kwargs)