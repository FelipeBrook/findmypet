# Generated by Django 4.2.5 on 2023-09-08 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0010_pet'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='especie',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='contacto',
            name='edad',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='mascota',
            name='edad',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='pet',
            name='edad',
            field=models.PositiveIntegerField(null=True),
        ),
    ]