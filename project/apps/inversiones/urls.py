from django.urls import path
from . import views

urlpatterns = [

    path('tipos-inversor/', views.lista_tipos_inversor, name='lista_tipos_inversor'),
    path('instrumentos-financieros/', views.lista_instrumentos_financieros, name='lista_instrumentos_financieros'),
]