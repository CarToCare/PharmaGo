from django.shortcuts import render

# Create your views here.
def principal(request):
    return render(request, 'principal.html')

def iniciar_sesion(request):
    return render(request, 'iniciar_sesion.html')

def inicio(request):
    return render(request, 'inicio.html')
