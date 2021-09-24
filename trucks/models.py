from django.db import models

from drivers.models import Driver

# Create your models here.

class Truck(models.Model):

    driver = models.ManyToManyField(Driver)

    unit =  models.IntegerField() 
    make = models.CharField(blank=True, max_length=100)
    plate = models.CharField(blank=True, max_length=100)
    type = models.CharField(blank=True, max_length=100)
    year = models.IntegerField()
    driver_1 = models.CharField(blank=True, max_length=100)
    driver_2 = models.CharField(blank=True, max_length=100)
    country = models.CharField(blank=True, max_length=100)
    state = models.CharField(blank=True, max_length=100)
    VIN_number = models.CharField(blank=True, max_length=100)
    terminal = models.CharField(blank=True, max_length=100)
    

    class CityTruckType(models.TextChoices):
        BOTH = 'BOTH'
        CITY = 'CITY'
        HIGHWAY_TRUCK = 'HGHWY'
    city_truck = models.CharField(max_length=5, choices=CityTruckType.choices, default=None, blank=True)
    
    tour = models.IntegerField()
    still_working = models.BooleanField(default=False)
    
    leave_date = models.DateField()
    
    class TruckOwnershipType(models.TextChoices):
        COMPANY_TRUCK = 'CMPNY_TRK'
        OWNER_OPERATORS_PAID_BY_MILE = 'ONR_OPRTR_PD_ML'
        PAID_BY_PERCENTAGE = 'PD_BY_PRCNTG'
    truck_ownership = models.CharField(max_length=15, choices=TruckOwnershipType.choices, default=None, blank=True)
    
    value = models.FloatField()
    weight_pounds = models.FloatField()
    IFTA_group = models.IntegerField()
    
    # Owner Operator Details
    account = models.CharField(blank=True, max_length=100)
    percentage = models.FloatField()
    rate_per_mile_LOAD = models.FloatField()
    rate_per_mile_EMPTY = models.FloatField()
    rate_per_hour = models.FloatField()

class TruckSafetyDetail(models.Model):
    truck = models.ForeignKey(Truck, on_delete=models.CASCADE)
    safety_details = models.CharField(blank=True, max_length=100)
    renewal_date = models.DateField()
    description = models.CharField(blank=True, max_length=100)
    stop_dispatch_on_expiry = models.BooleanField(default=False)


class TruckMonthlyDeduction(models.Model):
    truck = models.ForeignKey(Truck, on_delete=models.CASCADE)  
    monthly_deductions =  models.CharField(blank=True, max_length=100)
    day_of_month =  models.IntegerField()
    currency_CDN =  models.BooleanField(default=False)
    charges =  models.FloatField()
    valid_till =  models.DateField()
    belongs_to_company =  models.BooleanField(default=False)
    vendor =  models.CharField(blank=True, max_length=100)
    HST =  models.BooleanField(default=False)