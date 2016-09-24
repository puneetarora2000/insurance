from django.db.models.expressions import F

from polling.models import *
import faker
from autofixture import AutoFixture
from django.contrib.auth.models import User,Group
from datetime import datetime
from django.utils import timezone
import random


#     RegistrationID = models.ForeignKey(HospitalSubjectRegistration, models.DO_NOTHING, blank=True, null=True)
#     DataOfReading = models.DateTimeField(blank=True, verbose_name="Date of Reading")
#     SugarMonitoringDeviceReading = models.FloatField(default=0)
#     WorkOutMachineDeviceReading = models.FloatField(default=0)
#     PulseMonitorReading = models.FloatField(default=0)
#     TemperatureMonitorReading = models.FloatField(default=0)
#     SleepPatternsMonitorReading = models.FloatField(default=0)



def insertPatientHealth(count):
    fake = faker.Factory.create()
    for num in range(count):
        year = random.choice(range(2015, 2016))
        month = random.choice(range(1, 12))
        day = random.choice(range(1, 29))
        date_of_reading = datetime(year, month, day)
        timezone_date = timezone.make_aware(date_of_reading, timezone.get_current_timezone())
        registrationid = random.randint(3,4)
        health_data = HospitalInsuranceSubjectData(RegistrationID=HospitalSubjectRegistration.objects.\
                                get(id=registrationid),SugarMonitoringDeviceReading=random.randint(20,60), \
                                WorkOutMachineDeviceReading=random.randint(20,60), \
                                TemperatureMonitorReading=random.randint(360,720),DataOfReading=timezone_date)
        health_data.save()
        print("----Added Patient Health Data--------")
