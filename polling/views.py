

import json
from django.db.models import Avg
from django.views.decorators.csrf import csrf_protect ,csrf_exempt
from rest_framework import viewsets
from polling.serializers import *
from polling.forms import *
from django.shortcuts import get_object_or_404, render
from polling.models import HospitalSubjectRegistration, CadiacData
import faker
import random

@csrf_exempt
def cardiacpost(request):
    if request.method == 'GET':
        # do something
        return HttpResponse('You are in GET Method', content_type="application/json")
    elif request.method == "POST":
        bulk_data = request.body
        queryset = CadiacData(UserData=bulk_data)
        queryset.save()
        return HttpResponse(bulk_data, content_type="application/json")
    elif request.method == "DELETE":
        # do something
        return HttpResponse('You are in DELETE Method', content_type="application/json")
    else:
        # do something
        pass
# 1
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


# 2
class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


# 3
class ContactLoggingSerializerViewSet(viewsets.ModelViewSet):
    queryset = APIContactLogging.objects.all()
    serializer_class = ContactLoggingSerializer


# 4
class HospitalSubjectRegistrationSerializerViewSet(viewsets.ModelViewSet):
    queryset = HospitalSubjectRegistration.objects.all()
    serializer_class = HospitalSubjectRegistrationSerializer




# 6
class InsuraceOfficeRegistrationSerializerViewSet(viewsets.ModelViewSet):
    queryset = InsuraceOfficeRegistration.objects.all()
    serializer_class = InsuraceOfficeRegistrationSerializer


# 7
# class InsurancePremiumModellingViewSet(viewsets.ModelViewSet):
#     queryset = InsurancePremiumModelling.objects.all()
#     serializer_class = InsurancePremiumModellingSerializer


# 7
class InsuranceplancategoryViewSet(viewsets.ModelViewSet):
    queryset = Insuranceplancategory.objects.all()
    serializer_class = InsuranceplancategorySerializer



def patientrecord(request):
    form = HospitalSubjectRegistrationForm()
    return render(request,  'polling/patientrecord.html', {'form':form})

def  insuranccost(request):
    data = HospitalSubjectRegistration.objects.all()
    return render(request,  'polling/graphs.html', {'datalist':data})
# def devicerecord(request):
#     form = HospitalSubjectDeviceRegistrationForm()
#     return render(request,  'polling/devicerecord.html', {'form':form})
def creategraph(request, reg_id):

    SugarMonitoringDeviceReadingAvg = HospitalInsuranceSubjectData.objects.filter(RegistrationID=reg_id).aggregate(Avg('SugarMonitoringDeviceReading'))
    WorkOutMachineDeviceReadingAvg = HospitalInsuranceSubjectData.objects.filter(RegistrationID=reg_id).aggregate(Avg('WorkOutMachineDeviceReading'))
    PulseMonitorReadingAvg = HospitalInsuranceSubjectData.objects.filter(RegistrationID=reg_id).aggregate(Avg('PulseMonitorReading'))
    TemperatureMonitorReadingAvg = HospitalInsuranceSubjectData.objects.filter(RegistrationID=reg_id).aggregate(Avg('TemperatureMonitorReading'))
    SleepPatternsMonitorReadingAvg = HospitalInsuranceSubjectData.objects.filter(RegistrationID=reg_id).aggregate(Avg('SleepPatternsMonitorReading'))
    #data = [SugarMonitoringDeviceReadingAvg,WorkOutMachineDeviceReadingAvg,PulseMonitorReadingAvg,TemperatureMonitorReadingAvg,SleepPatternsMonitorReadingAvg]
    #fake = faker.Factory.create()
    index = random.choice(range(0, 1))
    ageindex = random.choice(range(0, 8))
    alindex = random.choice(range(0, 3))
    findex = random.choice(range(0,2))

    Gender = ['M','F']
    Age = [20,25,30,35,40,45,50,60,65,70]
    Marital = ['S','M']
    Alcohol = ['O','N','W','D']
    Family = ['1','2','3']
    Tobacco = ['Y','N']
    Profession = ['NH','H']
    AgeReward ={}
    SleepReward ={}
    M = {}
    AlcoholReward = {}
    FamilyReward = {}
    TobaccoReward = {}
    ProfessionReward = {}
    WorkOutReward ={}
    W = WorkOutMachineDeviceReadingAvg['WorkOutMachineDeviceReading__avg']
    S = SleepPatternsMonitorReadingAvg['SleepPatternsMonitorReading__avg']


    if(S>=8):
        SleepReward = {'SleepReward':10}
    else :
        SleepReward = {'SleepReward':5}


    if(W>=40):
        WorkOutReward = {'WorkOutReward':10}
    else :
        WorkOutReward = {'WorkOutReward':5}


    if(Gender[index]=='M'):
        if(Age[ageindex]>=20 & Age[ageindex]<=30):
            AgeReward = {'AgeReward':10}
        else :
            AgeReward = {'AgeReward':5}

    if(Marital[index]=='S'):
        print('**************')
        if(Age[ageindex]>=20 or Age[ageindex]<=30):
            M = {'M':10}
        else :
            M = {'M':5}

    if(Alcohol[alindex]=='N'):
        AlcoholReward = {'AlcoholReward':10}
    else :
        AlcoholReward = {'AlcoholReward':5}


    if(Family[findex]=='1'):
        FamilyReward = {'FamilyReward':10}
    else :
        FamilyReward = {'FamilyReward':5}

    if(Tobacco[index]=='N'):
       TobaccoReward = {'TobaccoReward':10}
    else :
       TobaccoReward = {'TobaccoReward':10}

    if(Profession[index]=='NH'):
        ProfessionReward = {'ProfessionReward':10}
    else :
        ProfessionReward = {'ProfessionReward':5}

    print(M)
   # data = dict(SugarMonitoringDeviceReadingAvg.items()+WorkOutMachineDeviceReadingAvg.items()+PulseMonitorReadingAvg.items()+TemperatureMonitorReadingAvg.items()+SleepPatternsMonitorReadingAvg.items())
    data = dict(SleepReward.items()+WorkOutReward.items()+M.items()+SleepPatternsMonitorReadingAvg.items()+ProfessionReward.items()+TobaccoReward.items()+FamilyReward.items()+AgeReward.items()+AlcoholReward.items())
   # print data
    return render(request,  'polling/creategraph.html',{'datalist':json.dumps(data)})


@csrf_exempt
def savesubjectsfromhospital(request):
    bulk_list ={}

    if request.method == 'POST':
        bulk_list = json.loads(request.body)
        #print(bulk_list["rows"])
         #Create a Object of Hospital Subject Registration :

        list = [HospitalSubjectRegistration(hospital_name_id=HopitalRegistration.objects.get(id=r["hospital_name_id"]),Patient_ID=r['Patient_ID'],FullName = r["FullName"],FullAddress = r["FullAddress"],Patient_History=r["Patient_History"],DoctorID=r["DoctorID"],RegisterPatientRemoteMonitoring=r["RegisterPatientRemoteMonitoring"]) for r in bulk_list['rows']]
        print(list)
        HospitalSubjectRegistration.objects.bulk_create(list)
    else:
        response_data = "Nothing to see"
    return HttpResponse(json.dumps(bulk_list['rows']), content_type="application/json" )


def csrf_failure(request, reason=""):
    ctx = {'message': 'some custom messages'}
    return render_to_response("template", ctx)



class CardiacViewSet(viewsets.ModelViewSet):
    queryset = CadiacData.objects.all()
    serializer_class = CardiacSerializer


# def create_post(request):
#     if request.method == 'POST':
#         post_text = request.POST.get('the_post')
#         response_data = {}
#
#         post = Post(text=post_text, author=request.user)
#         post.save()
#
#         response_data['result'] = 'Create post successful!'
#         response_data['postpk'] = post.pk
#         response_data['text'] = post.text
#         response_data['created'] = post.created.strftime('%B %d, %Y %I:%M %p')
#         response_data['author'] = post.author.username
#
#         return HttpResponse(
#             json.dumps(response_data),
#             content_type="application/json"
#         )
#     else:
#         return HttpResponse(
#             json.dumps({"nothing to see": "this isn't happening"}),
#             content_type="application/json"
#         )
#
#
# def delete_post(request):
#     if request.method == 'DELETE':
#
#         post = Post.objects.get(pk=int(QueryDict(request.body).get('postpk')))
#
#         post.delete()
#
#         response_data = {}
#         response_data['msg'] = 'Post was deleted.'
#
#         return HttpResponse(
#             json.dumps(response_data),
#             content_type="application/json"
#         )
#     else:
#         return HttpResponse(
#             json.dumps({"nothing to see": "this isn't happening"}),
#             content_type="application/json"
#         )


