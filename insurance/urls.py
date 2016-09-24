"""insurance URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

#rom polling.views import save_patients_devices


from django.conf.urls import url, include
from rest_framework import routers
from polling  import views

from rest_framework.authtoken import views as authviews
router = routers.DefaultRouter()
#8
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'contactlogging', views.ContactLoggingSerializerViewSet)
router.register(r'hdr', views.HospitalSubjectRegistrationSerializerViewSet)
router.register(r'insuranceoffice', views.InsuraceOfficeRegistrationSerializerViewSet)
#router.register(r'insurancepremium', views.InsurancePremiumModellingViewSet )
router.register(r'insuranceplan', views.InsuranceplancategoryViewSet )
router.register(r'cardiacdata', views.CardiacViewSet)
#router.register(r'insurancepremium', views.InsurancePremiumModellingViewSet )
#router.register(r'accounts', views.UserView, 'list')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-token-auth/', authviews.obtain_auth_token),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', include(router.urls)),
    #url(r'^docs/', include('rest_framework_swagger.urls')),
    url(r'^polling/', include('polling.urls', namespace="polling")),
    url(r'^cardiacpost/',views.cardiacpost,name="cardiacpost"),
]



