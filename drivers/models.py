from typing import ClassVar
from django.db import models

# Create your models here.


class Driver(models.Model):

    full_name = models.CharField(blank=True, max_length=100)
    address_street = models.CharField(blank=True, max_length=100)
    address_city = models.CharField(blank=True, max_length=100)
    address_state = models.CharField(blank=True, max_length=100)
    address_unit = models.CharField(blank=True, max_length=100)
    address_ZIP = models.CharField(blank=True, max_length=100)
    company = models.CharField(blank=True, max_length=100)
    phone_int = models.IntegerField()
    cellphone_Canada = models.IntegerField()
    cellphone_US = models.IntegerField()
    WCB = models.IntegerField()
    SSN = models.IntegerField()
    driver_paid_by_Company_OwnerOperator = models.CharField(blank=True, max_length=100)
    appointment_date = models.DateField()
    loadedMileRange_Alone = models.IntegerField()
    loadedMileRange_Team = models.IntegerField()
    emptyMileRange_Alone = models.IntegerField()
    emptyMileRange_Team = models.IntegerField()
    percentage_pay = models.BooleanField(default=False)
    perectage = models.FloatField()
    notes = models.CharField(blank=True, max_length=100)
    bank_details = models.CharField(blank=True, max_length=100)
    truck_int = models.IntegerField()
    CSA_FAST_Driver = models.BooleanField(default=False)
    pay_GST = models.BooleanField(default=False)
    deduct_taxes_on_pay = models.BooleanField(default=False)
    exempt_EI = models.BooleanField(default=False)
    exempt_CPP = models.BooleanField(default=False)
    claim_code = models.IntegerField()
    CRA_Tax_pay_periods_year = models.IntegerField()
    currently_working = models.BooleanField(default=False)
    leave_date = models.DateField()



class MonthlyDeductionTable(models.Model):

    monthly_deductions = models.CharField(blank=True, max_length=100)
    day_of_month = models.IntegerField()
    currency_CDN = models.BooleanField(default=False)
    charges = models.FloatField()
    less = models.BooleanField(default=False)
    valid_till = models.DateField()


class DriverNote(models.Model):

    date = models.DateField()
    incident = models.CharField(blank=True, max_length=100)
    note = models.CharField(blank=True, max_length=100)


class DriverSafety(models.Model):

    safety_details = models.CharField(blank=True, max_length=100)
    renewal_date = models.DateField()
    description = models.CharField(blank=True, max_length=100)
    stop_dispatch_on_expiry = models.BooleanField(default=False)