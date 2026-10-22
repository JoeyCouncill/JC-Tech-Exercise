from django.contrib import admin

from .models import Manufacturer, Vehicle, VehicleModel

admin.site.register(Manufacturer)
admin.site.register(VehicleModel)
admin.site.register(Vehicle)