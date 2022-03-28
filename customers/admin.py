from django.contrib import admin

from . models import Customers

@admin.register(Customers)
class CustomerAdmin(admin.ModelAdmin):
    list_display = [
        'full_name',
        'phone_number',
        'direction',
        'district',
        'reference',
        'is_regular_client',
        'is_active',
        'created',
        'updated',
    ]

    list_filter = [
        'is_active',
        'is_regular_client',
    ]
    list_editable=[
        'phone_number',
        'direction',
        'district',
        'reference',
        'is_regular_client',
        'is_active',
    ]
    