from django.db import models

# Create your models here.


class Driver(models.Model):
    email = models.EmailField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    mobile_number = models.PositiveSmallIntegerField()
    city = models.CharField(max_length=100,)
    district = models.CharField(max_length=100,)
    language = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
