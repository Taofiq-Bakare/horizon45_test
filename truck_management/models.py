from django.db import models


# Create your models here.


class Truck(models.Model):
    number_plate = models.CharField(max_length=15, unique=True)
    registration_number = models.CharField(max_length=15, unique=True)


class Driver(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100, null=False)
    mobile_number = models.PositiveSmallIntegerField()
    city = models.CharField(max_length=100, )
    district = models.CharField(max_length=100, )
    language = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    assigned_truck = models.OneToOneField(Truck, on_delete=models.CASCADE, related_name='driver',default=None, null=True, blank=True)
