import decimal
from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator

TYPE_CHOICES = (
        ('Natys Juane', 'Natys Juane'),
        ('Natys Bakery', 'Natys Bakery'),
        ('Natys Coffe', 'Natys Coffe'),
    )


class Product(models.Model):
    name = models.CharField(max_length=170, unique=True, blank=False)
    description = models.TextField(max_length=200)
    type = models.CharField(max_length=170 ,choices=TYPE_CHOICES, default="Natys Juane")
    unity = models.CharField(max_length=170)
    price = models.DecimalField(decimal_places=2, max_digits=12, validators=[MinValueValidator(decimal.Decimal('0.01'))])
    register_date = models.DateTimeField()

    def __str__(self) -> str:
        return self.name
    
    def save(self, *args, **kwargs):
        self.register_date = timezone.now()
        super(Product, self).save(*args, **kwargs)

    class Meta:
        ordering = ('-id',)