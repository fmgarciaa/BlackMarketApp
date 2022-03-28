from csv import list_dialects
from django.contrib import admin
from .models import Order, OrderItem

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'customer',
        'date',
        'pay_method',
        'bank',
        'total_pay',
        'status',
        'is_active'
    ]

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = [
        'order',
        'product',
        'quantity',
        'price',
        'is_active',
    ]
