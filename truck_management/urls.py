from django.urls import path
from truck_management import views

urlpatterns = [
    path('driver/', views.driver_list_create),
    path('driver/<int:driver_id>', views.driver_details)
]