# Generated by Django 4.2.11 on 2024-05-03 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0005_remove_webscraping_twitter'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresa',
            name='usernameAcercaDe',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
