from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TipoMascota(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
    

class RazaMascota(models.Model):
    nombre = models.CharField(max_length=100)
    tipo_mascota = models.ForeignKey(TipoMascota, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nombre
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=100, null=True)
    ciudad = models.CharField(max_length=50, null=True)
    imagen = models.ImageField(upload_to="perfil", null=True)
    

    def __str__(self):
        return self.user.username

class MascotaUser(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.ForeignKey(TipoMascota, on_delete=models.CASCADE)
    raza = models.ForeignKey(RazaMascota, on_delete=models.CASCADE)
    edad = models.PositiveIntegerField()
    dueño = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    imagen = models.ImageField(upload_to="mascotas", null=True)
    descripcion = models.TextField(max_length=200, null=True)
    detalles = models.TextField(max_length=200, null=True)
    

    def __str__(self):
        return self.nombre

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    edad= models.PositiveIntegerField(max_length=2, null=True)
    correo = models.EmailField(null=True)
    telefono = models.CharField(max_length=10)
    mensaje = models.TextField()
    list_per_page = 10


    def __str__(self):
        return self.nombre
    
class Mascota(models.Model):
    nombre = models.CharField(max_length=50)
    raza = models.CharField(max_length=50, null=True)
    imagen = models.ImageField(upload_to="mascotas", null=True)
    edad= models.PositiveIntegerField(max_length=2, null=True)
    list_per_page = 10
    def __str__(self):
        return self.nombre   





   

