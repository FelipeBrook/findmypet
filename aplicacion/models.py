from django.db import models

# Create your models here.

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





   

