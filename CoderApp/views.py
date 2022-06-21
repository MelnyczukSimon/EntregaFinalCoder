from django.shortcuts import render
from django.http import HttpResponse
from CoderApp.models import Abuela
from CoderApp.models import Perro
from CoderApp.models import Padre

# Create your views here.
def Familia(self):
      abuela= Abuela(nombre='norma lucia gomez', jubilada=True,cumpleanios='1930-03-19')
      abuela.save()
      perro = Perro  (nombre='simon jr',raza='caniche',edad=123)
      perro.save()
      padre = Padre (nombre='Eduardo',apellido='Melnyczuk',email='racingPasion@hotmal.com.ar',profesion='jardinero',cumpleanios='1960-01-01')
      padre.save()
      documentoDeTexto =f"{abuela.nombre},{abuela.jubilada},{abuela.cumpleanios},<br>{perro.nombre},{perro.raza},{perro.edad},<br>{padre.nombre},{padre.apellido},{padre.email},{padre.profesion},{padre.cumpleanios},"
      return HttpResponse(documentoDeTexto)

#def perro(self):
      perro = Perro  (nombre='simon jr',raza='caniche',edad=123)
      perro.save()
      documentoDeTexto =f"--->perro:{perro.nombre},{perro.raza}"
      return HttpResponse(documentoDeTexto)

#def padre(self):
      padre = Padre  (nombre='Eduardo',apellido='Melnyczuk',email='racingPasion@hotmal.com.ar',profesion='jardinero',cumpleanios='1960-01-01')
      padre.save()
      documentoDeTexto =f"--->padre:{padre.nombre},{padre.apellido},{padre.email},{padre.profesion},{padre.cumpleanios},"
      return HttpResponse(documentoDeTexto)
    