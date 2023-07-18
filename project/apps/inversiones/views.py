
from django.shortcuts import render
from .models import TipoInversor
from .models import InstrumentoFinanciero


def lista_tipos_inversor(request):
    tipos_inversor = TipoInversor.objects.all()
    return render(request, 'lista_tipos_inversor.html', {'tipos_inversor': tipos_inversor})


def lista_instrumentos_financieros(request):
    instrumentos_financieros = InstrumentoFinanciero.objects.all()
    return render(request, 'lista_instrumentos_financieros.html', {'instrumentos_financieros': instrumentos_financieros})