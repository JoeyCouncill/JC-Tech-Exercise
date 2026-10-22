from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models


class Manufacturer(models.Model):

    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class VehicleModel(models.Model):

    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.PROTECT, related_name="vehicle_models")
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ["manufacturer__name", "name"]
        constraints = [
            models.UniqueConstraint(fields=["manufacturer", "name"], name="unique_model_per_manufacturer"),
        ]

    def __str__(self):
        return f"{self.manufacturer} {self.name}"


class Vehicle(models.Model):

    vehicle_model = models.ForeignKey(VehicleModel, on_delete=models.PROTECT, related_name="vehicles")
    submodel = models.CharField(max_length=100, blank=True)
    year = models.PositiveSmallIntegerField(validators=[MinValueValidator(1886)])
    engine_size_litres = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        null=True,
        blank=True,
        validators=[MinValueValidator(0)],
        help_text="Engine displacement in litres; leave blank if not applicable.",
    )

    description = models.TextField(blank=True)

    class Meta:
        ordering = ["vehicle_model__manufacturer__name", "vehicle_model__name", "year"]
        constraints = [
            models.CheckConstraint(
                condition=(
                    models.Q(engine_size_litres__isnull=True)
                    | models.Q(engine_size_litres__gte=0)
                ),
                name="vehicle_engine_size_nonnegative",
            ),
        ]

    def __str__(self):
        name = f"{self.vehicle_model} {self.submodel}".strip()
        return f"{name} ({self.year})"