from django.urls import path

from . import views

app_name = "vehicletracker"

urlpatterns = [
    path("", views.vehicle_list, name="vehicle_list"),
    path("vehicles/add/", views.vehicle_create, name="vehicle_create"),
]