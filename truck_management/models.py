from django.db import models

# Create your models here.


class Driver(models.Model):
    email = models.EmailField(primary_key=True)
    name = models.CharField(max_length=100)
    mobile_number = models.PositiveIntegerField()
    city = models.CharField()
    district = models.CharField()
    language = models.CharField()
    created = models.DateTimeField(auto_now_add=True)
