from django.conf.urls import url

from . import views

app_name = 'polling'
urlpatterns = [
   url(r'^patientrecord/', views.patientrecord,name="patientrecord"),
   url(r'^savesubjectsfromhospital/', views.savesubjectsfromhospital,name="savesubjectsfromhospital"),
   url(r'^devicerecord/', views.savesubjectsfromhospital,name="devicerecord"),
   url(r'^insuranccost/',views.insuranccost,name="insuranccost"),
   url(r'^creategraph/(?P<reg_id>[0-9]+)$',views.creategraph,name="creategraph"),

   ]
