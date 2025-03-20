from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import usuarios_coll, proto_coll, entregas_coll
from .db import getOnePaciente, getPacientes

# Create your views here.
def principal(request):
    return render(request, 'principal.html')

def iniciar_sesion(request):
    return render(request, 'iniciar_sesion.html')

def inicio(request):
    return render(request, 'inicio.html')

def entregas(request):
    e=entregas_coll.find();
    return render(request, 'entregas.html', {'entregas': e})

def proto(request):
    p=proto_coll.find()
    print(p[0]['idUsuario'])
    return render(request, 'proto.html',{'proto':p[0]})

def medicamentos(request):
    return render(request, 'medicamentos.html')

def pacientes(request):
    pc=getPacientes()
    return render(request, 'pacientes.html', {'pacientes':pc});

def test(request):
    p=getPacientes("PAC-001")
    print(p)
    return HttpResponse(p)

def sIn(request):
    if request.method =='POST':
        email=request.POST.get('correo')    
        pas=request.POST.get('pass')
    u=usuarios_coll.find_one( {"correoElectronico":email})
    if u['password']==pas and u['pL']==True:
        user=User.objects.create_user(
            username=u['nombre'],
            password=u['password'],
            correo=u['correoElectronico'],
            telefono=u['datosComplementarios']['telefono']
        )
        user=authenticate(correo=u['correoElectronico'], password=u['password'])
        if user is not None:
            print("Usuario autenticado")
            
        else:
            print("Usuario o contraseña incorrectos")
    else:
        print("no existe")
    return HttpResponse(u)

