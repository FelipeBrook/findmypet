# Generated by Django 4.2.5 on 2023-09-06 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0003_rename_descripcion_mascota_raza'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='raza',
            field=models.CharField(max_length=50),
        ),
    ]