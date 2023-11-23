from typing import Any
from django.db import models
from django.contrib.auth.models import User


class Raza(models.Model):
    nombre = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.nombre

class Mascota(models.Model):
    TIPO_CHOICES = (
        ('perro', 'Perro'),
        ('gato', 'Gato'),
    )
    
    nombre = models.CharField(max_length=50)
    tamaño = models.CharField(max_length=10, null=True, choices=[('Grande', 'Grande'), ('Mediano', 'Mediano'), ('Pequeño', 'Pequeño')])
    edad = models.IntegerField()
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES, null=True)
    Raza = models.ForeignKey(Raza, on_delete=models.PROTECT, null=True)
    genero = models.CharField(max_length=10, null=True, choices=[('Macho', 'Macho'), ('Hembra', 'Hembra')])
    personalidad= models.CharField(max_length=50, null=True)
    miedos= models.CharField(max_length=50, null=True)
    vacunas =  models.CharField(max_length=10, null=True, choices=[('SI', 'SI'), ('NO', 'NO')])
    chip= models.CharField(max_length=10, null=True, choices=[('SI', 'SI'), ('NO', 'NO')])
    imagen = models.ImageField(upload_to="mascotas", null=True)
    imagen2 = models.ImageField(upload_to="mascotas", null=True)
    imagen3= models.ImageField(upload_to="mascotas", null=True)
    imagen4 = models.ImageField(upload_to="mascotas", null=True)
    imagen5 = models.ImageField(upload_to="mascotas", null=True)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre
    

class Marca(models.Model):
    nombre= models.CharField(max_length=50) 

    def __str__(self):
        return self.nombre
    

# CARRITO DE COMPRAS
class Cliente(models.Model):
    usuario= models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    nombre = models.CharField(max_length=200, null=True)
    email= models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre= models.CharField(max_length=50)
    precio = models.IntegerField()
    descripccion = models.TextField()
    marca=models.ForeignKey(Marca, on_delete=models.PROTECT)
    imagen= models.ImageField(upload_to="Alimentos", null=True)
     
    def __str__(self):
        return self.nombre



