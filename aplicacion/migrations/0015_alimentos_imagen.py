# Generated by Django 4.2.5 on 2023-11-18 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0014_marca_alimentos'),
    ]

    operations = [
        migrations.AddField(
            model_name='alimentos',
            name='imagen',
            field=models.ImageField(null=True, upload_to='Alimentos'),
        ),
    ]