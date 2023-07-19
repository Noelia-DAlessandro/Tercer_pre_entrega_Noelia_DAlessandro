from django.contrib import admin

# Register your models here.
# En el archivo admin.py de la aplicación 'inversiones'


from .models import TipoInversor, InstrumentoFinanciero

admin.site.register(TipoInversor)
admin.site.register(InstrumentoFinanciero)
