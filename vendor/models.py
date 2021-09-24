from django.db import models
from django.contrib.auth.models import User

class Vendor(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    full_name = models.CharField(blank=True, max_length=100)
    address_street = models.CharField(blank=True, max_length=100)
    address_city = models.CharField(blank=True, max_length=100)
    address_state = models.CharField(blank=True, max_length=100)
    address_unit = models.CharField(blank=True, max_length=100)
    address_ZIP = models.CharField(blank=True, max_length=100)
    EIN_number = models.CharField(blank=True, max_length=100)
    WCB_number = models.CharField(blank=True, max_length=100)
    phone_1 = models.IntegerField()
    phone_2 = models.IntegerField()
    fax_number = models.IntegerField()
    terms = models.CharField(blank=True, max_length=100)
    contact = models.CharField(blank=True, max_length=100)
    company = models.CharField(blank=True, max_length=100)
    email = models.EmailField(max_length = 254)
    website = models.CharField(blank=True, max_length=100)
    notes = models.CharField(blank=True, max_length=100)