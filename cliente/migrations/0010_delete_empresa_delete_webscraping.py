# Generated by Django 4.2.11 on 2024-05-15 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0009_alter_webscraping_acercade'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Empresa',
        ),
        migrations.DeleteModel(
            name='WebScraping',
        ),
    ]
