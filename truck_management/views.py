from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .models import Driver
from .serializers import DriverSerializer
from rest_framework.request import Request
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@api_view(["GET", "POST"])
def driver_create(request: Request):
    """
    Create driver.
    """
    if request.method == 'POST':
        #check if the driver already exists.
        if Driver.objects.filter(email=request.data.get('email')).exists():
            return Response({'error': 'Driver already exists'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = DriverSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
