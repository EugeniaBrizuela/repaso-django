# Generated by Django 4.0.3 on 2022-04-18 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_blogs_subtitulo_alter_blogs_titulo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='subtitulo',
            field=models.CharField(default=2, max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blogs',
            name='titulo',
            field=models.CharField(max_length=30),
        ),
    ]
