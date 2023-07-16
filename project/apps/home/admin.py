from django.contrib import admin
from django.db import models


# Register your models here.
from .models import Home, Pais

admin.site.register(Home)
admin.site.register(Pais)