# Generated by Django 4.2.5 on 2023-12-12 01:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0022_remove_mascota_ubicacion_escaneo_mascota_latitud_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Direccion',
        ),
    ]
