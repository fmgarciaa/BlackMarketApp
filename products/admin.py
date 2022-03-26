from django.contrib import admin

from .models import Product, Category, Unit

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'unit', 'price', 'category', 
                'create_by', 'in_stock', 'slug', 'created', 'updated', 'is_active']
    list_filter = ['is_active', 'in_stock']
    list_editable = ['price', 'in_stock', 'unit', 'is_active']
    prepopulated_fields = {'slug': ('name',)}