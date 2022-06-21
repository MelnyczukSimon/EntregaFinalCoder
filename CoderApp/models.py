from django.db import models

# Create your models here.
class Familia(models.Model):

    nombre = models.CharField(max_length=40)
    cantidad = models.IntegerField()
    direccion = models.CharField(max_length=20)
    


class Hijo(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    cumpleanios = models.DateField()

class Padre(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    profesion = models.CharField(max_length=30)
    cumpleanios = models.DateField()

class Abuela(models.Model):
    nombre = models.CharField(max_length=30) 
    jubilada = models.BooleanField()
    cumpleanios = models.DateField()

class Perro(models.Model):
    nombre = models.CharField(max_length=30)
    raza = models.CharField(max_length=20)
    edad = models.IntegerField()