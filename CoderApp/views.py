from django.shortcuts import render
from CoderApp.models import Planta
from CoderApp.models import Arbol
from CoderApp.models import Cactus
from CoderApp.forms import CursoFormulario

def Inicio(request):
     return render(request,"CoderApp/Inicio.html")

def planta(request):
     planta = Planta.objects.all()
     print(planta)
     return render(request,"CoderApp/planta.html",{'planta':planta})

def arbol(request):
     arbol = Arbol.objects.all()
     print(arbol)
     return render(request,"CoderApp/arbol.html",{'arboles':arbol})

def cactus(request):
     cactus = Cactus.objects.all()
     print(cactus)
     return render(request,"CoderApp/cactus.html",{'cactus':cactus})

def cursoFormulario(request):

      if request.method == 'POST':

            miFormulario = CursoFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data
                  print(informacion)
                  planta = Planta (nombre=informacion['nombre'], nombreCientifico =informacion['raza']) 

                  planta.save()

                  return render(request, "CoderApp/inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= CursoFormulario() #Formulario vacio para construir el html

      return render(request, "CoderApp/cursoFormulario.html", {"miFormulario":miFormulario})



