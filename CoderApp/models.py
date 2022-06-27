from django.db import models

# Create your models here.
class Planta(models.Model):
    nombre = models.CharField(max_length=40)
    nombreCientifico = models.CharField(max_length=40)
    cantidad = models.IntegerField()
    deInterior = models.CharField(max_length=40)
    
class Arbol(models.Model):
    nombre = models.CharField(max_length=40)
    nombreCientifico = models.CharField(max_length=40)
    alturaMax = models.IntegerField()

class Cactus(models.Model):
    nombre = models.CharField(max_length=30)
    nombreCientifico = models.CharField(max_length=40)
    tiempoSinAgua = models.IntegerField()