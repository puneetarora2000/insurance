from django.shortcuts import render

# Create your views here.

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from polling.serializers import *

#1
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
#2
class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
#3
class  ContactLoggingSerializerViewSet(viewsets.ModelViewSet):
    queryset = ContactLogging.objects.all()
    serializer_class = ContactLoggingSerializer
#4
class  HospitalSubjectDeviceRegistrationSerializerViewSet(viewsets.ModelViewSet):
    queryset = HospitalSubjectDeviceRegistration.objects.all()
    serializer_class = HospitalSubjectDeviceRegistrationSerializer
#5
class  HospitalSubjectRegistrationSerializerViewSet(viewsets.ModelViewSet):
    queryset = HospitalSubjectRegistration.objects.all()
    serializer_class = HospitalSubjectRegistrationSerializer

#6
class  InsuraceOfficeRegistrationSerializerViewSet(viewsets.ModelViewSet):
    queryset = InsuraceOfficeRegistration.objects.all()
    serializer_class = InsuraceOfficeRegistrationSerializer
#7
class  InsurancePremiumModellingViewSet(viewsets.ModelViewSet):
    queryset = InsurancePremiumModelling.objects.all()
    serializer_class = InsurancePremiumModellingSerializer
#7
class  InsuranceplancategoryViewSet(viewsets.ModelViewSet):
    queryset = Insuranceplancategory.objects.all()
    serializer_class = InsuranceplancategorySerializer
