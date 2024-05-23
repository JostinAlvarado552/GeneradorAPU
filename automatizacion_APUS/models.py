from django.db import models

class Rubros(models.Model):
    id = models.IntegerField(primary_key=True)
    concepto = models.TextField(null=True, blank=True)
    unidad = models.CharField(max_length=20, null=True, blank=True)

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
    contenido = models.TextField(blank=True, null=True)  # Cambiado a TextField
