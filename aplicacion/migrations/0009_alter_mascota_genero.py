# Generated by Django 4.2.5 on 2023-10-05 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0008_raza_remove_mascota_raza_perro_mascota_raza'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='genero',
            field=models.CharField(choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino')], max_length=10, null=True),
        ),
    ]