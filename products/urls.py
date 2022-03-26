from importlib.resources import path
from django.urls import path


from . import views

app_name='product'
urlpatterns = [
    path('products/', views.ProductList.as_view(template_name='products/index.html'), name='index'),
    
]