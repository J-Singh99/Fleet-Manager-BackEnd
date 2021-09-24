from django.contrib import admin
from .models import Truck, TruckSafetyDetail, TruckMonthlyDeduction

admin.site.register(TruckMonthlyDeduction)
admin.site.register(TruckSafetyDetail)
admin.site.register(Truck)