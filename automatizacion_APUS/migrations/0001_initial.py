# Generated by Django 4.1.7 on 2024-05-18 23:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rubros',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('categoria', models.CharField(max_length=80, null=True)),
                ('concepto', models.CharField(max_length=100, null=True)),
                ('especificaciones', models.CharField(max_length=30, null=True)),
                ('rendimiento', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Medicion_Pago',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('medicion', models.CharField(max_length=130)),
                ('metodoPago', models.CharField(max_length=130)),
                ('rubro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='automatizacion_APUS.rubros')),
            ],
        ),
        migrations.CreateModel(
            name='Especificacion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('contenido', models.CharField(max_length=130)),
                ('rubro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='automatizacion_APUS.rubros')),
            ],
        ),
        migrations.CreateModel(
            name='Definicion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('contenido', models.CharField(max_length=130)),
                ('rubro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='automatizacion_APUS.rubros')),
            ],
        ),
    ]
