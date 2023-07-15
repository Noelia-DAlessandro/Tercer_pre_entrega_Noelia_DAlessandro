from django.contrib import admin
from django.db import models


# Register your models here.
from .models import Cliente, Pais

admin.site.register(Cliente)
admin.site.register(Pais)