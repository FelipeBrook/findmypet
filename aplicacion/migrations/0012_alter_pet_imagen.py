# Generated by Django 4.2.5 on 2023-09-08 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0011_pet_especie_alter_contacto_edad_alter_mascota_edad_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='imagen',
            field=models.ImageField(null=True, upload_to='pet_photos'),
        ),
    ]
