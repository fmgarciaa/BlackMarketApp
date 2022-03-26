from django.db import models
from django.core.exceptions import ValidationError

def phone_validate(value):
    if len(value) >= 10:
        raise ValidationError('phone must be 9 max character')
    if not value.isnumeric():
        raise ValidationError('phone must be only number')

class Customers(models.Model):
    full_name = models.CharField(max_length=255, unique=True, blank=False)
    phone_number = models.CharField(max_length=9, validators=[phone_validate])
    direction = models.CharField(max_length=255)
    district = models.CharField(max_length=255, blank=False)
    reference = models.CharField(max_length=255)
    is_regular_client = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.full_name
    
    class Meta:
        verbose_name_plural = 'customers'
        ordering = ('-created',)
