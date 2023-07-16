from django.db import models
 
class Pais(models.Model):
    nombre = models.CharField(max_length=50)
 
    def __str__(self):
        return self.nombre

class Usuario (models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    nacimiento = models.DateField(null=True)
    pais_origen_id = models.ForeignKey(Pais, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f"{self.nombre} {self.apellido}"