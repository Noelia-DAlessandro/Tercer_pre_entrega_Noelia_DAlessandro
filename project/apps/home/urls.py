from django.urls import path
from . import views, crear_cliente  



urlpatterns = [
    path('', views.index),
    path('crear/',crear_cliente, name="crear")
]