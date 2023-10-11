# Generated by Django 4.2.5 on 2023-10-05 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0006_mascota_genero_mascota_imagen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mascota',
            name='raza',
        ),
        migrations.AddField(
            model_name='mascota',
            name='raza_perro',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='mascota',
            name='tipo',
            field=models.CharField(choices=[('perro', 'Perro'), ('gato', 'Gato')], max_length=10, null=True),
        ),
    ]
