# Generated by Django 5.0 on 2023-12-09 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='receta',
            name='origen',
            field=models.CharField(max_length=100, null=True, verbose_name='Origen'),
        ),
    ]
