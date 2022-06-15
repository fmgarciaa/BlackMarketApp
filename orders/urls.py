from django.urls import path

from . import views
from . import invoice_generator

app_name='order'
urlpatterns = [
    path('order/create', views.all_products, name='create'),
    path('order/checkout', views.checkout_order, name='checkout'),
    path('order/list', views.all_orders, name='list'),
    path('order/delete/<int:pk>', views.OrderDelete.as_view(), name='delete'),
    path('order/update/<int:pk>', views.UpdateOrder.as_view(template_name='orders/update.html'), name='update'),
    path('order/update_items/<int:id>', views.update_items, name='items_update'),
    path('order/modify', views.modify_order, name='modify'),
    path('order/invoice/<int:id>', invoice_generator.some_view, name='invoice'),
]
