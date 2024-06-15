from .models import  Driver


class DriverRepository:
    @staticmethod
    def get_driver_bi_id(driver_id:int):
        try:
            return Driver.objects.get(pk=driver_id)
        except Driver.DoesNotExist:
            return None