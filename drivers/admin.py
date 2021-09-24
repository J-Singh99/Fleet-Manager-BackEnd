from django.contrib import admin
from .models import Driver, MonthlyDeductionTable, DriverNote, DriverSafety



admin.site.register(Driver)
admin.site.register(MonthlyDeductionTable)
admin.site.register(DriverNote)
admin.site.register(DriverSafety)