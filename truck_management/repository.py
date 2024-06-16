from .models import Driver
from .serializers import DriverSerializer
from django.db import transaction
from rest_framework.exceptions import ValidationError

class DriverRepository:
    @staticmethod
    def get_driver_by_id(driver_id: int):
        try:
            return Driver.objects.get(pk=driver_id)
        except Driver.DoesNotExist:
            return None

    @staticmethod
    def get_all_drivers(filters=None):
        if filters is None:
            filters = {}
        return Driver.objects.filter(**filters)

    @staticmethod
    def create_driver(data):
        serializer = DriverSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return serializer.data, None
        return None, serializer.errors

    @staticmethod
    def create_bulk_drivers(drivers_data):
        created_drivers = []
        errors = []

        with transaction.atomic():
            for driver_data in drivers_data:
                serializer = DriverSerializer(data=driver_data)
                if serializer.is_valid():
                    created_driver = serializer.save()
                    created_drivers.append(DriverSerializer(created_driver).data)
                else:
                    errors.append(serializer.errors)

            if errors:
                # If there are errors, roll back the transaction
                raise ValidationError(errors)

        return created_drivers


