# Generated by Django 4.2.21 on 2025-06-27 22:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0011_alter_muestrabiologica_latitud_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='muestrabiologica',
            name='familia',
        ),
    ]
