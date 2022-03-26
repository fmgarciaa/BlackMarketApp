from django.urls import path

from . import views

app_name='cart'
urlpatterns = [
    path('', views.cart_summary, name='cart_summary'),
    path("add/<int:product_id>/", views.add_product, name="add_item"),
    path("increase/<int:product_id>/", views.increase_quantity, name="increase"),
    path("delete/<int:product_id>/", views.delete_product, name="delete_item"),
    path("remove/<int:product_id>/", views.remove_product, name="remove_item"),
    path("clean/", views.clear_cart, name="clean_cart"),
]