from django.contrib import admin
from .models import Trailer, TrailerSafetyDetail, TrailerMonthlyDeduction, TrailerRepairService



admin.site.register(Trailer)
admin.site.register(TrailerSafetyDetail)
admin.site.register(TrailerMonthlyDeduction)
admin.site.register(TrailerRepairService)