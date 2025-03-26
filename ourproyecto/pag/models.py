from django.contrib.auth.models import AbstractUser
from django.db import models
from db_con import db

usuarios_coll=db['usuarios']
med_coll=db['medicamentos']
proto_coll=db['prototipos']
entregas_coll=db['entregas']
pacientes_coll=db['pacientes']
recetas_coll=db['recetas']

class CustomUser(AbstractUser):
    # Campos adicionales
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)

    USERNAME_FIELD = 'correo'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.correo