# Generated by Django 4.2.1 on 2023-06-03 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laboratorio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='fecha_alta',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de alta AAAA-MM-DD'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='fecha_baja',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de baja AAAA-MM-DD'),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='fecha_alta',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de alta AAAA-MM-DD'),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='fecha_baja',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de baja AAAA-MM-DD'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='fecha_alta',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de alta AAAA-MM-DD'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='fecha_baja',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de baja AAAA-MM-DD'),
        ),
    ]
