from django.urls import path
from CoderApp import views
urlpatterns=[
    path('',views.Inicio,name='Inicio'),#esta-era-nuestra-primer-view
    path('cursos',views.cursos,name='cursos'),
    path('profesores',views.profesores,name='profesores'),
    path('estudiantes',views.estudiantes,name='estudiantes'),
    path('entregables',views.entregables,name='entregables'),
    ]