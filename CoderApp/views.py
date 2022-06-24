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

def inicio(request):
    return render(request,"CoderApp/inicio.html")

def cursos(request):
     return render(request,"CoderApp/cursos.html")

def profesores(request):
     return render(request,"CoderApp/profesores.html")

def estudiantes(request):
      return render(request,"CoderApp/estudiantes.html")

def entregables(request):
      return render(request,"CoderApp/entregables.html")
