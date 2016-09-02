from django.contrib import admin

# Register your models here.
from .models import *

from django.contrib import admin
from polling.forms import *


class PollsAdmin(admin.ModelAdmin):
   # fields = ('hospital_detail','hospital_user_name','api_token_key')
   # fields = "__all__"
  #  list_filter = ('id' )
   # list_display = 'id'
    #search_fields = ('id',)
    form = RegisterSubjectForm





admin.site.register(HospitalSubjectDeviceRegistration, PollsAdmin)

admin.site.register(InsurancePremiumModelling)
admin.site.register(InsuraceOfficeRegistration)


admin.site.register(HospitalSubjectRegistration)
#admin.site.register(HospitalSubjectDeviceRegistration)
admin.site.register(ContactLogging)
admin.site.register(Insuranceplancategory)
admin.site.register(SensorDeviceType)



