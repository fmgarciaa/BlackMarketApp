from django.urls import path
from . import views


app_name='dashboard'
urlpatterns = [
    path('dashboard/list', views.dashboardView, name='index'),
]