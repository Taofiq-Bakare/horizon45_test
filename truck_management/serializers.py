from rest_framework import serializers
from .models import Driver,Truck

class TruckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Truck
        fields = "__all__"


class DriverSerializer(serializers.ModelSerializer):
    assigned_truck = TruckSerializer()
    class Meta:
        model = Driver
        fields = "__all__"

    def create(self, validated_data):
        truck_data = validated_data.pop('assigned_truck')
        truck = Truck.objects.create(**truck_data)
        driver = Driver.objects.create(assigned_truck=truck, **validated_data)
        return driver
