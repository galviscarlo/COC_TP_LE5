# Generated by Django 5.0 on 2023-12-09 22:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_receta_origen'),
    ]

    operations = [
        migrations.RenameField(
            model_name='receta',
            old_name='descripcion',
            new_name='preparacion',
        ),
    ]
