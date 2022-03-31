from importlib.resources import path
from django.urls import path


from . import views

app_name='product'
urlpatterns = [
    path('products/', views.ProductList.as_view(template_name='products/index.html'), name='index'),
    path('products/delete/<slug:slug>', views.ProductDelete.as_view(), name='delete'),
    path('products/update/<slug:slug>', views.ProductUpdate.as_view(template_name='products/update.html'), name='update'),
    path('products/create', views.ProductCreate.as_view(template_name='products/create.html'), name='create'),
]