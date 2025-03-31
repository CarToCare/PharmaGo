from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import usuarios_coll, proto_coll, entregas_coll, CustomUser, recetas_coll, med_coll, pacientes_coll
from .db import getOnePaciente, getPacientes
import re

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

def nuevo_idRec():
    ultima_rec = recetas_coll.find_one(sort=[("idReceta", -1)])

    if ultima_rec:
        ultimo_id = ultima_rec["idReceta"]
        numero = int(ultimo_id.split("-")[1])  # Extrae el número de "REC-002"
        nuevo_numero = numero + 1
    else:
        nuevo_numero = 1  # Si no hay recetas, empieza desde 1

    return f"REC-{nuevo_numero:03d}"  # Formato: REC-001, REC-002, etc.

def registroRec(request):
    nuevo_id_rec = nuevo_idRec()
    pacientes = pacientes_coll.find()
    medicamentos = med_coll.find()
    
    return render(request, 'registroRec.html', {
        'nuevo_id_rec': nuevo_id_rec,
        'pacientes' : pacientes,
        'medicamentos': medicamentos
    })

def regRec(request):
    if request.method == 'POST':
        idReceta = request.POST.get('idReceta')
        idPaciente = request.POST.get('idPaciente')

        medicamentos = []
        index = 0
        while f"medicamentos[{index}][idMedicamento]" in request.POST:
            medicamento = {
                "idMedicamento": request.POST.get(f"medicamentos[{index}][idMedicamento]"),
                "cantidad": int(request.POST.get(f"medicamentos[{index}][cantidad]")),
                "horaInicial": request.POST.get(f"medicamentos[{index}][horaInicial]"),
                "periodicidad": request.POST.get(f"medicamentos[{index}][periodicidad]"),
                "fechaInicio": request.POST.get(f"medicamentos[{index}][fechaInicio]"),
                "fechaFin": request.POST.get(f"medicamentos[{index}][fechaFin]"),
            }
            medicamentos.append(medicamento)
            index += 1

        receta = {
            "idReceta": idReceta,
            "idPaciente": idPaciente,
            "medicamentos": medicamentos
        }

        recetas_coll.insert_one(receta)

        return redirect('recetas')  # Redirigir a la página de recetas después de registrar

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

def generar_id_paciente():
    ultimo_paciente = pacientes_coll.find_one({}, sort=[("idPaciente", -1)])

    if ultimo_paciente and "idPaciente" in ultimo_paciente:
        match = re.search(r'PAC-(\d+)', ultimo_paciente["idPaciente"])
        if match:
            nuevo_numero = int(match.group(1)) + 1
            return f"PAC-{nuevo_numero:03d}"

    return "PAC-001"

def regPac(request):
    if request.method == 'POST':
        id_paciente = request.POST.get('idPaciente')
        nombre_paciente = request.POST.get('nombrePaciente')
        fecha_nacimiento = request.POST.get('fechaNacimientoPaciente')
        cama_paciente = int(request.POST.get('camaPaciente')) 
        alergias = request.POST.get('alergiasPaciente').split(',')
        riesgo_caida = request.POST.get('riesgoCaida')
        genero_paciente = request.POST.get('generoPaciente')
        habitacion_paciente = int(request.POST.get('habitacionPaciente')) 

        id_paciente = generar_id_paciente()

        data = {
            'idPaciente': id_paciente,
            'nombrePaciente': nombre_paciente,
            'fechaNacimientoPaciente': fecha_nacimiento,
            'camaPaciente': cama_paciente,
            'alergiasPaciente': alergias,
            'riesgoCaida': riesgo_caida,
            'generoPaciente': genero_paciente,
            'habitacionPaciente': habitacion_paciente,
            'status': True,
        }

        pacientes_coll.insert_one(data)

        return redirect('pacientes')

    return render(request, 'registro.html')

def recetas(request):
    r = recetas_coll.find()
    return render(request, 'recetas.html', {'recetas': r})
