from django.urls import path
from CoderApp import views
urlpatterns=[
    path('',views.Inicio,name='Inicio'),#esta-era-nuestra-primer-view
    path('planta',views.planta,name='planta'),
    path('arbol',views.arbol,name='arbol'),
    path('cactus',views.cactus,name='cactus'),
    path('cursoFormulario',views.cursoFormulario,name="cursoFormulario"),
 ]