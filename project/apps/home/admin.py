from django.contrib import admin
from . import models


# Register your models here.
from .models import Usuario, Pais

admin.site.register(Usuario)
admin.site.register(Pais)