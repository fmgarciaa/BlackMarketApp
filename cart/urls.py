from importlib.resources import path
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

from . views import *

app_name='cart'
urlpatterns = [
    path('cart/', TemplateView.as_view(template_name="cart/cart.html"), name='home'),
    path('add/<int:product_id>/', add_product, name='add'),
    path('delete/<int:product_id>/', delete_product, name='delete'),
    path('remove/<int:product_id>/', remove_product, name='remove'),
    path('sum/<int:product_id>/', sum_product, name='sum'),
    path('clean/', clean_cart, name='clean'),
    
]