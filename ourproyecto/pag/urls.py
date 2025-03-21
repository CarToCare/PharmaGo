from django.urls import path
from . import views

urlpatterns = [
    path('', views.principal, name='principal'),
    path('sesion/', views.sesion, name='sesion'),
    path('inicio/', views.inicio, name='inicio'),
    path('proto/', views.proto, name='proto'),
    path('medicamentos/', views.medicamentos, name='medicamentos'),
    path('pacientes/', views.pacientes, name='pacientes'),
    path('registro/', views.registro, name='registro'),
]
