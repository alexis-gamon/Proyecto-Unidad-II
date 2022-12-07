# Generated by Django 4.1.3 on 2022-11-30 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculos', '0003_remove_almacen_localidad_almacen_modelo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='almacen',
            name='NumAlmacen',
            field=models.CharField(blank=True, max_length=14, null=True),
        ),
        migrations.AddField(
            model_name='entregas',
            name='Entrega',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='almacen',
            name='Modelo',
            field=models.CharField(blank=True, max_length=14, null=True),
        ),
    ]
