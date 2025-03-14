from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User
from .models import usuarios_coll

# Create your views here.
def principal(request):
    return render(request, 'principal.html')

def iniciar_sesion(request):
    return render(request, 'iniciar_sesion.html')

def inicio(request):
    return render(request, 'inicio.html')

def sIn(request):
    if request.method =='POST':
        email=request.POST.get('correo')    
        pas=request.POST.get('pass')
    u=usuarios_coll.find_one( {"correoElectronico":email})
    return HttpResponse(u)