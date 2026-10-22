from django.urls import path

from . import views

urlpatterns = [
    path("", views.Vehicle_list, name="vehicle_list"),
    path("vehicles/add/", views.vehicle_create, name="vehicle_create")
]