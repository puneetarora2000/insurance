from django.contrib.auth.models import User, Group
from polling.models import *
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class ContactLoggingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model =  ContactLogging
        fields = ('ContactLogging', 'LastUpdate')

class HospitalSubjectDeviceRegistrationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HospitalSubjectDeviceRegistration
        fields = ('SmokingMedium', 'LastUpdate')

class HospitalSubjectRegistrationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HospitalSubjectRegistration
        fields = ('PhysicalActivitySpeed', 'LastUpdate')

        #InsuraceOfficeRegistration
class InsuraceOfficeRegistrationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = InsuraceOfficeRegistration
        fields = ('SystolicReading','DiastolicReading','LastDateOfTest','LastUpdate')

        #InsurancePremiumModelling
class InsurancePremiumModellingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = InsurancePremiumModelling
        fields = ('WhichDrink','FatInTake','FoodSupliment','LastUpdate')


#CholesterolReading

class InsuranceplancategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Insuranceplancategory
        fields = ('LowDensityLipoProtein','VeryLowDensityLipoProtein','HighDensityLipoProtein','TriglyceridesReadings','TotalCholesterol','LastDateOfTest','LastUpdate')
