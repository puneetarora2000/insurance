from django.contrib import admin

# Register your models here.
from .models import *


admin.site.register(InsurancePremiumModelling)
admin.site.register(InsuraceOfficeRegistration)
admin.site.register(HospitalSubjectRegistration)
admin.site.register(HospitalSubjectDeviceRegistration)
admin.site.register(ContactLogging)
admin.site.register(Insuranceplancategory)
admin.site.register(SensorDeviceType)



