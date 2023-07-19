from django.db import models

# Create your models here.

class TipoInversor(models.Model):
    OPCIONES_INVERSOR = (
        ('conservador', 'Conservador'),
        ('agresivo', 'Agresivo'),
    )
    tipo = models.CharField(max_length=20, choices=OPCIONES_INVERSOR)

    def __str__(self):
        return self.tipo

class InstrumentoFinanciero(models.Model):
    OPCIONES_INSTRUMENTO = (
        ('plazo_fijo', 'Plazo fijo'),
        ('bonos', 'Bonos'),
        ('acciones', 'Acciones'),
    )

    OPCIONES_CAMBIO = (
        ('pesos', 'Pesos'),
        ('dolares', 'Dólares'),
    )

    tipo = models.CharField(max_length=20, choices=OPCIONES_INSTRUMENTO)
    tipo_cambio = models.CharField(max_length=10, choices=OPCIONES_CAMBIO)

    def __str__(self):
        return f"{self.get_tipo_display()} - {self.get_tipo_cambio_display()}"