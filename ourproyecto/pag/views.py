from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User
from .models import usuarios_coll, proto_coll, entregas_coll

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

def sIn(request):
    if request.method =='POST':
        email=request.POST.get('correo')    
        pas=request.POST.get('pass')
    u=usuarios_coll.find_one( {"correoElectronico":email})
    return HttpResponse(u)

def proto(request):
    p=proto_coll.find()
    print(p[0]['idUsuario'])
    return render(request, 'proto.html',{'proto':p[0]})

def medicamentos(request):
    return render(request, 'medicamentos.html')
