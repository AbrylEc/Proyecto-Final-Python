# Generated by Django 4.1.3 on 2022-11-20 08:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('biography', '0002_alter_biography_published'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='biography',
            options={'ordering': ['created'], 'verbose_name': 'evento', 'verbose_name_plural': 'eventos'},
        ),
    ]