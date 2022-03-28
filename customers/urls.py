from importlib.resources import path
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from customers.views import *

app_name='customer'
urlpatterns = [
    path('customer/', CustomerList.as_view(template_name="customers/index.html"), name='list'),
    path('customer/detail/<int:pk>', CustomerDetail.as_view(template_name='customers/detail.html'), name='detail'),
    path('customer/create', CustomerCreate.as_view(template_name='customers/create.html'), name='create'),
    path('customer/edit/<int:pk>', CustomerUpdate.as_view(template_name='customers/update.html'), name='update'),
    path('customer/delete/<int:pk>', CustomerDelete.as_view(), name='delete'),
]