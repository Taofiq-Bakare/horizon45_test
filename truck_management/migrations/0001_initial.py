# Generated by Django 5.0.6 on 2024-06-16 08:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Truck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_plate', models.CharField(max_length=15, unique=True)),
                ('registration_number', models.CharField(max_length=15, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('mobile_number', models.PositiveSmallIntegerField()),
                ('city', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=100)),
                ('language', models.CharField(max_length=20)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('assigned_truck', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='driver', to='truck_management.truck')),
            ],
        ),
    ]
