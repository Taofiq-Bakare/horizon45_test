# Generated by Django 5.0.6 on 2024-06-15 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('truck_management', '0002_alter_driver_mobile_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='driver',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
