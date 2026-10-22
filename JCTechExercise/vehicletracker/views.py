from django.shortcuts import render, redirect
from .models import Manufacturer, Vehicle, VehicleModel
from .forms import VehicleForm


def vehicle_list(request):
    vehicles = Vehicle.objects.select_related(
        "vehicle_model__manufacturer"
    )

    manufacturer = request.GET.get("manufacturer", "")
    model = request.GET.get("model", "")
    year = request.GET.get("year", "")

    if manufacturer.isdigit():
        vehicles = vehicles.filter(
            vehicle_model__manufacturer_id=int(manufacturer)
        )

    if model.isdigit():
        vehicles = vehicles.filter(vehicle_model_id=int(model))

    if year.isdigit():
        vehicles = vehicles.filter(year=int(year))

    return render(request, "vehicletracker/vehicle_list.html", {
        "vehicles": vehicles,
        "manufacturers": Manufacturer.objects.all(),
        "models": VehicleModel.objects.all(),
        "selected_manufacturer": manufacturer,
        "selected_model": model,
        "selected_year": year,
    })

def vehicle_create(request):
    form = VehicleForm(
        request.POST if request.method == "POST" else None
    )

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("vehicle_list")

    return redirect("vehicletracker:vehicle_list")