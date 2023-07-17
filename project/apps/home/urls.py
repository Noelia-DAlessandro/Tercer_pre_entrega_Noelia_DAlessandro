from django.urls import path
from . import views
from .views import crear_cliente


urlpatterns = [
    path('', views.index, name = "Home"),
    path('crear/',crear_cliente, name="crear")
]