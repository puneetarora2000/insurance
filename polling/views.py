from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from django.http import QueryDict
# Create your views here.
import json
import requests
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from polling.serializers import *
from polling.forms import *
from . import authentication, serializers  # see previous post[1] for user serializer
from django.shortcuts import redirect
from . import authentication, serializers  # see previous post[1] for user serializer.
from django.http import Http404

# def HospitalSubjectDeviceRegistration(request,RegistedHospitalID):
#     try:
#         data = HospitalSubjectDeviceRegistration.objects.get(pk=RegistedHospitalID)
#     except HospitalSubjectDeviceRegistration.DoesNotExist:
#         raise Http404('Comprehension does not exist')
#     return render(request,  'polling/templates/deviceregistration.html', {'deviceregisration': data})


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
    queryset = ContactLogging.objects.all()
    serializer_class = ContactLoggingSerializer


# 4
class HospitalSubjectDeviceRegistrationSerializerViewSet(viewsets.ModelViewSet):
    queryset = HospitalSubjectDeviceRegistration.objects.all()
    serializer_class = HospitalSubjectDeviceRegistrationSerializer


# 5
class HospitalSubjectRegistrationSerializerViewSet(viewsets.ModelViewSet):
    queryset = HospitalSubjectRegistration.objects.all()
    serializer_class = HospitalSubjectRegistrationSerializer


# 6
class InsuraceOfficeRegistrationSerializerViewSet(viewsets.ModelViewSet):
    queryset = InsuraceOfficeRegistration.objects.all()
    serializer_class = InsuraceOfficeRegistrationSerializer


# 7
class InsurancePremiumModellingViewSet(viewsets.ModelViewSet):
    queryset = InsurancePremiumModelling.objects.all()
    serializer_class = InsurancePremiumModellingSerializer


# 7
class InsuranceplancategoryViewSet(viewsets.ModelViewSet):
    queryset = Insuranceplancategory.objects.all()
    serializer_class = InsuranceplancategorySerializer




def create_post(request):
    if request.method == 'POST':
        post_text = request.POST.get('the_post')
        response_data = {}

        post = Post(text=post_text, author=request.user)
        post.save()

        response_data['result'] = 'Create post successful!'
        response_data['postpk'] = post.pk
        response_data['text'] = post.text
        response_data['created'] = post.created.strftime('%B %d, %Y %I:%M %p')
        response_data['author'] = post.author.username

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )


def delete_post(request):
    if request.method == 'DELETE':

        post = Post.objects.get(pk=int(QueryDict(request.body).get('postpk')))

        post.delete()

        response_data = {}
        response_data['msg'] = 'Post was deleted.'

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )

def save_patients_devices(request):

    if request.method == "POST":
        form = HospitalSubjectDeviceRegistrationForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            r = requests.get('http://127.0.0.0:9000/patients/id' + url)
            json = r.json()
            serializer = HospitalSubjectDeviceRegistrationSerializer (data=json)
            if serializer.is_valid():
                data = serializer.save()
                return render(request, 'pat_device.html', {'data': data})
    else:
        form = HospitalSubjectDeviceRegistrationForm()

    return render(request, 'index.html', {'form': form})