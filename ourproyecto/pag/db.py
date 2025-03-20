from .models import pacientes_coll, proto_coll, usuarios_coll, med_coll, recetas_coll, entregas_coll

def getOnePaciente(id):
    p=pacientes_coll.find_one({'idPaciente':id})
    return p;

def getPacientes():
    p=pacientes_coll.find()
    return p;
