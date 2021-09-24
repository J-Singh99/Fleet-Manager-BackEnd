from django.db import models
from trucks.models import Truck
# Create your models here.


class Trailer(models.Model):

    truck = models.ManyToManyField(Truck)

    unit = models.IntegerField()
    year = models.IntegerField()
    unit_tracking = models.IntegerField()
    make = models.CharField(blank=True, max_length=100)
    VIN_number = models.IntegerField()
    plate_number = models.IntegerField()
    country = models.CharField(blank=True, max_length=100)
    state = models.CharField(blank=True, max_length=100)
    weight_pounds = models.FloatField()
    # vehicle_type = TL
    value = models.FloatField()
    still_working = models.BooleanField(default=False)
    leave_date = models.DateField()


class TrailerSafetyDetail(models.Model):
    trailer = models.ForeignKey(Trailer, on_delete=models.CASCADE)
    safety_detail = models.CharField(blank=True, max_length=100)
    renewal_date = models.DateField()
    description = models.CharField(blank=True, max_length=100)
    stop_dispatch_on_expiry = models.BooleanField(default=False)


class TrailerMonthlyDeduction(models.Model):
    trailer = models.ForeignKey(Trailer, on_delete=models.CASCADE)
    monthly_deduction = models.CharField(blank=True, max_length=100)
    day_of_month = models.IntegerField()
    currency_CDN = models.BooleanField(default=False)
    charges = models.FloatField()
    valid_till = models.DateField()
    vendor = models.CharField(blank=True, max_length=100)
    HST = models.BooleanField(default=False)


class TrailerRepairService(models.Model):
    trailer = models.ForeignKey(Trailer, on_delete=models.CASCADE)
    date = models.DateField()
    type_service = models.CharField(blank=True, max_length=100)
    note = models.CharField(blank=True, max_length=100)