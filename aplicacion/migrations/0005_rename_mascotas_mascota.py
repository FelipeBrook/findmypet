# Generated by Django 4.2.5 on 2023-10-05 21:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0004_rename_mascota_mascotas'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Mascotas',
            new_name='Mascota',
        ),
    ]
