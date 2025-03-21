from django.shortcuts import render

# Create your views here.
def principal(request):
    return render(request, 'principal.html')

def sesion(request):
    return render(request, 'sesion.html')

def inicio(request):
    return render(request, 'inicio.html')

def proto(request):
    return render(request, 'proto.html')

def medicamentos(request):
    return render(request, 'medicamentos.html')

def pacientes(request):
    return render(request, 'pacientes.html')

def registro(request):
    return render(request, 'registro.html')

