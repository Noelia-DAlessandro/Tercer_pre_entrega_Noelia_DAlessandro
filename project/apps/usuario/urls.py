from django.urls import path
from . import views 

#urls de usuario - es la app que se va a conectar a home

app_name="usuario"


urlpatterns = [
    path('', views.index),
]