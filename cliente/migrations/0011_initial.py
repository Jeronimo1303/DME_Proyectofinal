# Generated by Django 4.2.11 on 2024-05-15 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cliente', '0010_delete_empresa_delete_webscraping'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('usernameComputrabajo', models.CharField(blank=True, max_length=100, null=True)),
                ('usernameInstagram', models.CharField(blank=True, max_length=100, null=True)),
                ('usernameFacebook', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='WebScraping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('instagram', models.JSONField(blank=True, null=True)),
                ('facebook', models.JSONField(blank=True, null=True)),
                ('computrabajo', models.JSONField(blank=True, null=True)),
                ('acercaDe', models.TextField(null=True)),
            ],
        ),
    ]