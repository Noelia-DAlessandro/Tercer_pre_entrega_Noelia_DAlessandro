from django.urls import path
from . import views 
#urls de home- es la app troncal


urlpatterns = [
    path('', views.index),
]