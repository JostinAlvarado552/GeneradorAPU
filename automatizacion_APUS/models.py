from django.db import models

class Rubros(models.Model):
    id = models.IntegerField(primary_key=True)
    categoria = models.CharField(max_length=80, null=True, blank=True)
    concepto = models.CharField(max_length=100, null=True, blank=True)
    especificaciones = models.CharField(max_length=100, null=True, blank=True)
    rendimiento = models.FloatField()

class Definicion(models.Model):
    id = models.AutoField(primary_key=True)
    rubro = models.ForeignKey(Rubros, on_delete=models.CASCADE)
    contenido = models.CharField(max_length=130, null=True, blank=True)

class Especificacion(models.Model):
    id = models.AutoField(primary_key=True)
    rubro = models.ForeignKey(Rubros, on_delete=models.CASCADE)
    contenido = models.CharField(max_length=130, null=True, blank=True)

class Medicion_Pago(models.Model):
    id = models.AutoField(primary_key=True)
    rubro = models.ForeignKey(Rubros, on_delete=models.CASCADE)
    medicion = models.CharField(max_length=130, blank=True, null=True)
    metodoPago = models.CharField(max_length=130, blank=True, null=True)