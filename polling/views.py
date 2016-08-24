from django.shortcuts import render

# Create your views here.

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from polling.serializers import *

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class  ContactLoggingSerializerViewSet(viewsets.ModelViewSet):
    queryset = ContactLogging.objects.all()
    serializer_class = ContactLoggingSerializer

class  HospitalSubjectDeviceRegistrationSerializerViewSet(viewsets.ModelViewSet):
    queryset = HospitalSubjectDeviceRegistration.objects.all()
    serializer_class = HospitalSubjectDeviceRegistrationSerializer

class  HospitalSubjectRegistrationSerializerViewSet(viewsets.ModelViewSet):
    queryset = HospitalSubjectRegistration.objects.all()
    serializer_class = HospitalSubjectRegistrationSerializer


class  InsuraceOfficeRegistrationSerializerViewSet(viewsets.ModelViewSet):
    queryset = InsuraceOfficeRegistration.objects.all()
    serializer_class = InsuraceOfficeRegistrationSerializer

class  InsurancePremiumModellingViewSet(viewsets.ModelViewSet):
    queryset = InsurancePremiumModelling.objects.all()
    serializer_class = InsurancePremiumModellingSerializer


