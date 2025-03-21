from django.urls import path
from . import views

urlpatterns = [
    path('', views.principal, name='principal'),
    path('sesion/', views.sesion, name='sesion'),
    path('inicio/', views.inicio, name='inicio'),
    path('sIn/',views.sIn, name="sIn"),
    path('proto/', views.proto, name='proto'),
    path('entregas/',views.entregas,name='entregas'),
    path('medicamentos/', views.medicamentos, name='medicamentos'),
    path('test/',views.test),
    path('pacientes/', views.pacientes, name='pacientes'),
    path('registro/', views.registro, name='registro'),
    path('recetas/', views.recetas, name='recetas'),

]
