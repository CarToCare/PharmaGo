from django.urls import path
from . import views

urlpatterns = [
    path('', views.principal, name='principal'),
    path('iniciar_sesion/', views.iniciar_sesion, name='iniciar_sesion'),
    path('inicio/', views.inicio, name='inicio'),
    path('medicamentos/', views.medicamentos, name='medicamentos'),
]
