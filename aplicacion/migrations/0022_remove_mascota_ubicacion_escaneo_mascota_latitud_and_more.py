# Generated by Django 4.2.5 on 2023-12-12 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0021_mascota_ubicacion_escaneo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mascota',
            name='ubicacion_escaneo',
        ),
        migrations.AddField(
            model_name='mascota',
            name='latitud',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mascota',
            name='longitud',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
