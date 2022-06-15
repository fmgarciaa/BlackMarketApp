from importlib.resources import path
from django.urls import path


from . import views

app_name='route'
urlpatterns = [
    path('route/', views.routeview, name='index'),
    path('route/', views.get_route, name='get_route'),
]