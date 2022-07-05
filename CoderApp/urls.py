from django.urls import path
from .import views
#app_name='CoderApp'
urlpatterns=[
    path('',views.inicio,name='inicio'),#esta-era-nuestra-primer-view
    path('planta',views.planta,name='planta'),
    path('arbol',views.arbol,name='arbol'),
    path('cactus',views.cactus,name='cactus'),
    path('registrarArbol',views.registrarArbol,name='registrarArbol'),
    path('registrarPlanta',views.registrarPlanta,name='registrarPlanta'),
    path('registrarCactus',views.registrarCactus,name='registrarCactus'),
    path('busqueda',views.busqueda,name='busqueda'),
 ]