# Generated by Django 4.1.7 on 2024-05-23 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('automatizacion_APUS', '0004_alter_rubros_rendimiento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='definicion',
            name='contenido',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='especificacion',
            name='contenido',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='medicion_pago',
            name='medicion',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='medicion_pago',
            name='metodoPago',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='rubros',
            name='especificaciones',
            field=models.TextField(blank=True, null=True),
        ),
    ]
