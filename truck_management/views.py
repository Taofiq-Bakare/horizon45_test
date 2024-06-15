from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .models import Driver
from .serializers import DriverSerializer
from rest_framework.request import Request
from .repository import DriverRepository


# Create your views here.

@api_view(["GET"])
def driver_details(request: Request, driver_id: int):
    driver = DriverRepository.get_driver_bi_id(driver_id=driver_id)
    if not driver:
        return Response(data=f"There is no driver with the id_no= {driver_id}", status=status.HTTP_404_NOT_FOUND)

    serializer = DriverSerializer(driver)
    return Response(serializer.data)


@api_view(["GET", "POST"])
def driver_list_create(request: Request):
    """
    List and create drivers.
    """
    if request.method == 'GET':
        # Retrieve filters from query parameters
        filters = {
            'email': request.query_params.get('email'),
            'mobile_number': request.query_params.get('mobile_number'),
            'language': request.query_params.get('language'),
            'assigned_truck__number_plate': request.query_params.get('number_plate')
        }

        # Remove None values from filters
        filters = {k: v for k, v in filters.items() if v is not None}

        # Get filtered drivers
        existing_drivers = Driver.objects.filter(**filters)

        # Serialize and return the data
        serializer = DriverSerializer(existing_drivers, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        # Check if the driver already exists
        if Driver.objects.filter(email=request.data.get('email')).exists():
            return Response({'error': 'Driver already exists'}, status=status.HTTP_400_BAD_REQUEST)

        # Deserialize and save the new driver
        serializer = DriverSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
def driver_bulk_create(request: Request):
    drivers_data = request.data
    created_drivers = []
    for driver in drivers_data:
        serializer = DriverSerializer(data=driver)
        if serializer.is_valid():
            serializer.save()
            created_drivers.append(serializer.data)
    return Response(created_drivers,status=status.HTTP_201_CREATED)
