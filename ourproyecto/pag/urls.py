from django.urls import path
from . import views

urlpatterns = [
    path('', views.principal, name='principal'),
    path('sesion/', views.sesion, name='sesion'),
    path('inicio/', views.inicio, name='inicio'),
    path('sIn/',views.sIn, name="sIn"),
    path('cerrar_sesion/', views.cerrar_sesion, name='cerrar_sesion'),
    path('proto/', views.proto, name='proto'),
    path('entregas/',views.entregas,name='entregas'),
    path('medicamentos/', views.medicamentos, name='medicamentos'),
    path("agregar_movimiento/", views.agregar_movimiento, name="agregar_movimiento"),
    path("formulario_movimiento/", views.formulario_movimiento, name="formulario_movimiento"),
    path('test/',views.test),
    path('pacientes/', views.pacientes, name='pacientes'),
    path('eliminar_paciente/<str:idPaciente>/', views.eliminar_paciente, name='eliminar_paciente'),
    path('registro/', views.registro, name='registro'),
    path('recetas/', views.recetas, name='recetas'),
    path('regPac/', views.regPac, name='regPac'),
    path('registroRec/', views.registroRec, name='registroRec'),
    path('regRec/', views.regRec, name='regRec'),
]
