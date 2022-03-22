from ast import Add
from importlib.resources import path
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

from orders.views import *

app_name='order'
urlpatterns = [
    path('order/', TemplateView.as_view(template_name="order/home.html"), name='home'),
    path('order/create', OrderCreate.as_view(template_name="order/create.html"), name='create'),
    path('order/orderitem', OrderItem.as_view(template_name="order/orderitem.html"), name='orderitem'),
    path('order/index', OrderList.as_view(template_name="order/index.html"), name='list'),
    path('order/detail/<int:pk>', OrderDetail.as_view(template_name='order/detail.html'), name='detail'),
    path('order/edit/<int:pk>', OrderUpdate.as_view(template_name='order/update.html'), name='update'),
    path('order/delete/<int:pk>', OrderDelete.as_view(), name='delete'),
    path('order/save/<int:pk>', save_order, name='save'),
]
