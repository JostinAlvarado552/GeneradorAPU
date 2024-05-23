from django.db import models

class Rubros(models.Model):
    id = models.IntegerField(primary_key=True)
    categoria = models.CharField(max_length=80, null=True, blank=True)
    concepto = models.CharField(max_length=100, null=True, blank=True)
    especificaciones = models.TextField(null=True, blank=True)  # Cambiado a TextField
    rendimiento = models.FloatField()

class Definicion(models.Model):
    id = models.AutoField(primary_key=True)
    rubro = models.ForeignKey(Rubros, on_delete=models.CASCADE)
    contenido = models.TextField(null=True, blank=True)  # Cambiado a TextField

class Especificacion(models.Model):
    id = models.AutoField(primary_key=True)
    rubro = models.ForeignKey(Rubros, on_delete=models.CASCADE)
    contenido = models.TextField(null=True, blank=True)  # Cambiado a TextField

class Medicion_Pago(models.Model):
    id = models.AutoField(primary_key=True)
    rubro = models.ForeignKey(Rubros, on_delete=models.CASCADE)
    medicion = models.TextField(blank=True, null=True)  # Cambiado a TextField
    metodoPago = models.TextField(blank=True, null=True)  # Cambiado a TextField
