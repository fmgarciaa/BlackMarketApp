from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from orders.models import *

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', include('products.urls')),
    path('', include('customers.urls')),
    path('', include('orders.urls')),
   ]


