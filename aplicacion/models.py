from django.db import models
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

