from .models import Driver
from .serializers import DriverSerializer


class DriverRepository:
    @staticmethod
    def get_driver_bi_id(driver_id: int):
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
        for driver in drivers_data:
            serializer = DriverSerializer(data=driver)
            if serializer.is_valid():
                serializer.save()
                created_drivers.append(serializer.data)
        return created_drivers
