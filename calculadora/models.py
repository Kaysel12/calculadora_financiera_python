from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    dias_operativos_in = models.IntegerField()
    dias_operativos_out = models.IntegerField()
    dias_reinversion_in = models.IntegerField()
    dias_reinversion_out = models.IntegerField()
    hora_operativa = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

class DiaFeriado(models.Model):
    fecha = models.DateField()
    descripcion = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.fecha.strftime('%Y-%m-%d')
