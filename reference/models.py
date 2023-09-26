from django.db import models


class VehicleType(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    yearManufactured = models.PositiveIntegerField()

    def __str__(self):
        return f" Vehicle type id : {self.id}"


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    vehicleType = models.ForeignKey(VehicleType, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    availability_status = models.BooleanField(default=True)

    def __str__(self):
        return f"Product id : {self.id} with name {self.name}"
