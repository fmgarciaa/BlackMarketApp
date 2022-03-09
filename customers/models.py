from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError

def phone_validate(value):
    if len(value) <= 9:
        raise ValidationError('phone must be 9 max character')
    if not value.isnumeric():
        raise ValidationError('phone must be only number')


DISTRICT_CHOICES = (
    ('1','Ate'),
    ('2','Barranco'),
    ('3','Breña'),
    ('4','Chorrillos'),
    ('5','Cieneguilla'),
    ('6','Comas'),
    ('7','El Agustino'),
    ('8','Independencia'),
    ('9','Jesus Maria'),
    ('10','La Molina'),
    ('11','La Victoria'),
    ('12','Lince'),
    ('13','Los Olivos'),
    ('14','San Juan de Lurigancho'),
    ('15','Magdalena del Mar'),
    ('16','Miraflores'),
    ('17','Pachacamac'),
    ('18','Lima'),
    ('19','Pueblo Libre'),
    ('20','Rimac'),
    ('21','San Borja'),
    ('22','San Isidro'),
    ('23','San Juan de Miraflores'),
    ('24','San Luis'),
    ('25','San Martín de Porres'),
    ('26','San Miguel'),
    ('27','Santa Anita'),
    ('28','Santiago de Surco'),
    ('29','Surquillo'),
    ('31','Villa El Salvador'),
    ('32','Villa María del Triunfo'),
)

class Customers(models.Model):
    full_name = models.CharField(max_length=179, unique=True, blank=False)
    phone_number = models.CharField(max_length=9, validators=[phone_validate])
    direction = models.CharField(max_length=170)
    district = models.CharField(max_length=27, choices=DISTRICT_CHOICES, blank=False)
    reference = models.CharField(max_length=170)
    is_regular_client = models.BooleanField(default=0)
    register_date = models.DateTimeField()

    def __str__(self) -> str:
        return self.name
    
    def save(self, *args, **kwargs):
        self.register_date = timezone.now()
        super(Customers, self).save(*args, **kwargs)

    class Meta:
        ordering = ('-id',)
