from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import usuarios_coll, proto_coll, entregas_coll, CustomUser, recetas_coll, med_coll
from .db import getOnePaciente, getPacientes

# Create your views here.
def principal(request):
    return render(request, 'principal.html')

def sesion(request):
    return render(request, 'sesion.html')

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
    med = med_coll.find()
    return render(request, 'medicamentos.html', {'medicamentos': med})

def pacientes(request):
    pc=getPacientes()
    return render(request, 'pacientes.html', {'pacientes':pc});

def test(request):
    p=getPacientes("PAC-001")
    print(p)
    return HttpResponse(p)

def sIn(request):
    print("hay va")
    if request.method =='POST':
        email=request.POST.get('correo')    
        pas=request.POST.get('pass')
    u=usuarios_coll.find_one( {"correoElectronico":email})
    if u is not None:
        if u['password']==pas and u['pL']==True:
            try:
                user = CustomUser.objects.get(correo=u['correoElectronico'])
            except CustomUser.DoesNotExist:
                user = CustomUser.objects.create_user(
                    username=u['nombre'],
                    password=u['password'],
                    correo=u['correoElectronico'],
                    telefono=u['datosComplementarios']['telefono']
                )
            user=authenticate(correo=u['correoElectronico'], password=u['password'])
            print(user.password)
            if user is not None:
                login(request,user)
                response=redirect('inicio')
                response.set_cookie('correo', email)
                print("Usuario autenticado")
            else:
                print("Usuario o contraseña incorrectos")
        else:
            print("no existe")
            response=redirect('principal')
    else:
        print("no existe")
        response=redirect('principal')
    return response

def registro(request):
    return render(request, 'registro.html')

def recetas(request):
    r = recetas_coll.find()
    return render(request, 'recetas.html', {'recetas': r})
