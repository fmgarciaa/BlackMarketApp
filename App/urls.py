from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', include('products.urls')),
    path('', include('customers.urls')),
    path('', include('orders.urls')),
    path('cart/', include('cart.urls', namespace='cart')),
   ]


