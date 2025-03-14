from django.db import models
from db_con import db

usuarios_coll=db['usuarios']
med_coll=db['medicamentos']
proto_coll=db['prototipo']
entregas_coll=db['entregas']
pacientes_coll=db['pacientes']
recetas_coll=db['recetas']