# Generated by Django 4.0.3 on 2022-03-20 23:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clases', '0003_alter_tienda_caracteristicas'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='fecha_publicacion',
        ),
    ]
