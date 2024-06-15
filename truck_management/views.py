from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .models import Driver
from .serializers import DriverSerializer
from rest_framework.request import Request
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

@api_view(["GET"])
def driver_details(request: Request, driver_id: int):
    try:
        driver = Driver.objects.get(pk=driver_id)
    except Driver.DoesNotExist:
        return Response(data=f"There is no driver with the id_no= {driver_id}", status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = DriverSerializer(driver)
        return Response(serializer.data)


@api_view(["GET", "POST"])
def driver_list_create(request: Request):
    """
    Create driver.
    """
    if request.method == 'GET':
        # retrieve filters for email, mobile_number, language
        ##todo assigned truck number plate.

        email = request.query_params.get('email')
        mobile_number = request.query_params.get('mobile_number')
        language = request.query_params.get('language')

        # get all existing drivers
        existing_drivers = Driver.objects.all()

        # apply filters
        if email:
            existing_drivers = existing_drivers.filter(email=email)
        if mobile_number:
            existing_drivers = existing_drivers.filter(mobile_number=mobile_number)
        if language:
            existing_drivers = existing_drivers.filter(language=language)

        serializer = DriverSerializer(existing_drivers, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        # check if the driver already exists.
        if Driver.objects.filter(email=request.data.get('email')).exists():
            return Response({'error': 'Driver already exists'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = DriverSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
