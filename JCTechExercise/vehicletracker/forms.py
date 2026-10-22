from django import forms

from .models import Vehicle


class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = [
            "vehicle_model",
            "submodel",
            "year",
            "engine_size_litres",
            "description",
        ]