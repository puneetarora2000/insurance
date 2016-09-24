from django import forms
from django.utils.safestring import mark_safe
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.views import generic

from polling.models import *


# hospital subject device registration



class ButtonWidget(forms.Widget):
    template_name = 'auth_button_widget.html'

    def render(self, name, value, attrs=None):
        context = {
            'url': 'http://localhost:9000/patients/'
        }
        return mark_safe(render_to_string(self.template_name, context))

#No Use , Useless
class RegisterSubjectForm(forms.ModelForm):
    FetchHospitalData = forms.CharField(widget=ButtonWidget)

    class Meta:
        model = HospitalSubjectRegistration
        exclude = []


# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         # exclude = ['author', 'updated', 'created', ]
#         fields = ['text']
#         widgets = {
#             'text': forms.TextInput(
#                 attrs={'id': 'post-text', 'required': True, 'placeholder': 'Say something...'}
#             ),
#         }


class HospitalSubjectRegistrationForm(forms.ModelForm):
    # url = forms.URLField()
    class Meta:
        model = HospitalSubjectRegistration
        exclude = ['FullName','Patient_ID','FullAddress','Patient_History','DoctorID','InsurancePolicyID','RegisterPatientRemoteMonitoring','InsurancePlan']



class HealthDataForm(forms.ModelForm):
    # url = forms.URLField()
    class Meta:
        model = HospitalInsuranceSubjectData
        exclude = ['SugarMonitoringDeviceReading','WorkOutMachineDeviceReading','PulseMonitorReading','TemperatureMonitorReading','SleepPatternsMonitorReading','DataOfReading']




# class DeviceForm(forms.ModelForm):
#     # url = forms.URLField()
#     class Meta:
#         model = DeviceRegister
#         exclude = ['subject_detail', 'subject_insurance_policy_detail', 'medical_history_brief', 'Patient_History',
#                    'device_details', 'RegisterPatientRemoteMonitoring']
