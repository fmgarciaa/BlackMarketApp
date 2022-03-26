from django.urls import path

from . import views

app_name='order'
urlpatterns = [
    path('order/create', views.all_products, name='create'),
]
