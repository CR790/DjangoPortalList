from enum import unique
from django.db import models


# Create your models here.

class Profesor(models.Model):
    codProfesor = models.IntegerField(primary_key=True, null=False, unique = True)
    usuarioci = models.ForeignKey(to='administracion.Usuario',on_delete=models.CASCADE, null=False)
    cargo = models.CharField(max_length=255, null=False)
    antiguedad = models.CharField(max_length=255, null=False)
    cedula = models.IntegerField(null=False, unique=True)
    nombre = models.CharField(max_length=255, null=False)
    usuario = models.CharField(max_length=255, null=False)
    #contrasenia, lo maneja django (?)
    apellido = models.CharField(max_length=255, null=False)
    nombre = models.CharField(max_length=255, null=False)
    email  = models.EmailField(max_length=70,blank=True,unique=True)
    codadministrador = models.ForeignKey(to='adminsitracion.Administrador',on_delete=models.CASCADE, null=False)


    def __str__(self):
        return self.codProfesor



class Lista(models.Model):
    codLista = models.IntegerField(primary_key=True, null=False)
    falta = models.BooleanField(default=False, null=False)
    justificada = models.BooleanField(default=False, null=False)
    llegada_tarde = models.BooleanField(default=False, null=False)

    def __str__(self):
        return self.codLista

class Materia(models.Model):
    codMateria = models.IntegerField(primary_key=True, null=False)
    nombre = models.CharField(max_length=255, null=False)
    horario = models.IntegerField()
    cod_profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.codMateria