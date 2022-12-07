# Generated by Django 4.1.3 on 2022-12-07 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculos', '0006_ubicacion_hora_ubicacion_lugar_alter_vehiculos_color_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehiculos',
            name='Precio',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ubicacion',
            name='CodigoPostal',
            field=models.CharField(max_length=5),
        ),
    ]
