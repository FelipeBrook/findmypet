# Generated by Django 4.2.5 on 2023-10-12 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0012_alter_mascota_chip_alter_mascota_genero_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='chip',
            field=models.CharField(choices=[('SI', 'SI'), ('NO', 'NO')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='mascota',
            name='vacunas',
            field=models.CharField(choices=[('SI', 'SI'), ('NO', 'NO')], max_length=10, null=True),
        ),
    ]
