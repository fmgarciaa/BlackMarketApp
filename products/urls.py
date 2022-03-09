from importlib.resources import path
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from products.views import *

app_name='product'
urlpatterns = [
    path('product/', ProductList.as_view(template_name="product/index.html"), name='list'),
    path('product/detail/<int:pk>', ProductDetail.as_view(template_name='product/detail.html'), name='detail'),
    path('product/create', ProductCreate.as_view(template_name='product/create.html'), name='create'),
    path('product/edit/<int:pk>', ProductUpdate.as_view(template_name='product/update.html'), name='update'),
    path('product/delete/<int:pk>', ProductDelete.as_view(), name='delete'),
]