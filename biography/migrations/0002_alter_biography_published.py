# Generated by Django 4.1.3 on 2022-11-20 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biography', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='biography',
            name='published',
            field=models.CharField(max_length=200, verbose_name='Fecha'),
        ),
    ]
