from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    full_name = models.CharField(blank=True, max_length=100)
    address_street = models.CharField(blank=True, max_length=100)
    address_city = models.CharField(blank=True, max_length=100)
    address_state = models.CharField(blank=True, max_length=100)
    address_unit = models.CharField(blank=True, max_length=100)
    address_ZIP = models.CharField(blank=True, max_length=100)
    phone_1 = models.IntegerField()
    phone_2 = models.IntegerField()
    fax_number = models.IntegerField()
    terms = models.CharField(blank=True, max_length=100)
    contact = models.CharField(blank=True, max_length=100)
    customer_broker = models.CharField(blank=True, max_length=100)
    quickpay = models.FloatField()
    email = models.EmailField(max_length = 254)
    website = models.CharField(blank=True, max_length=100)
    notes = models.CharField(blank=True, max_length=100)
    timings = models.CharField(blank=True, max_length=100)
    sales_person = models.CharField(blank=True, max_length=100)
    factor_invoices = models.BooleanField(default=False)
    CSA_FAST_approved = models.BooleanField(default=False)
    credit_limit = models.FloatField()
    customer_type = models.CharField(blank=True, max_length=100)