# Generated by Django 4.2.5 on 2023-10-05 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0005_rename_mascotas_mascota'),
    ]

    operations = [
        migrations.AddField(
            model_name='mascota',
            name='genero',
            field=models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='mascota',
            name='imagen',
            field=models.ImageField(null=True, upload_to='mascotas'),
        ),
    ]