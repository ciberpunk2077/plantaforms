# Generated by Django 4.2.21 on 2025-06-18 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0007_alter_muestrabiologica_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='muestrabiologica',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='get_upload_path_imagen', verbose_name='Imagen de la muestra'),
        ),
    ]
