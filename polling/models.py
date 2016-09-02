from __future__ import unicode_literals
from django.contrib.auth.models import User

from distutils.command.config import config

from django.db import models

import constants as constant
# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.



class ContactLogging(models.Model):
    #id = models.IntegerField(blank=True, null=True)
    contact = models.ForeignKey('PublishSubscribeContact', models.DO_NOTHING, blank=True, null=True)
    start_datetime = models.DateTimeField(blank=True, null=True)
    end_datetime = models.DateTimeField(blank=True, null=True)
    measurement = models.FloatField(blank=True, null=True)
    interval = models.FloatField(blank=True, null=True,default=6000)

    class Meta:
        managed = True
        db_table = 'contact_logging'


class HospitalSubjectDeviceRegistration(models.Model):
    #id = models.IntegerField(blank=True, null=True)
    hospital_name_id = models.ForeignKey('HospitalSubjectRegistration', models.DO_NOTHING, blank=True, null=True)
    subject_detail = models.TextField()
    subject_insurance_policy_detail = models.TextField(blank=True, null=True)
    medical_history_brief = models.TextField(blank=True, null=True)
    device_details = models.TextField(blank=True, null=True,verbose_name="Device DataSheet")
    lastupdate = models.DateTimeField(db_column='LastUpdate',auto_now_add=True)  # Field name made lowercase.
    class Meta:
        managed = True
        db_table = 'hospital_subject_device_registration'


class HospitalSubjectRegistration(models.Model):
    #id = models.IntegerField(blank=True, null=True)
    hospital_detail = models.TextField(blank=True, null=True)
    hospital_user_name = models.CharField(max_length=222)
    api_token_key = models.CharField(max_length=222, blank=True, null=True)
    isactive = models.NullBooleanField(db_column='isActive', blank=True, null=True)  # Field name made lowercase.
    isverified = models.NullBooleanField(db_column='isVerified', blank=True, null=True)  # Field name made lowercase.
    lastupdate = models.DateTimeField(db_column='LastUpdate',auto_now_add=True)  # Field name made lowercase.
    def __unicode__(self):
		return str(self.hospital_detail)
    class Meta:
        managed = True
        db_table = 'hospital_subject_registration'


class InsuraceOfficeRegistration(models.Model):
    #id = models.IntegerField(blank=True, null=True)
    insurance_office = models.CharField(max_length=100, blank=True, null=True)
    api_private_key = models.CharField(max_length=200, blank=True, null=True)
    api_public_key = models.CharField(max_length=200, blank=True, null=True)
    api_consumer_key = models.CharField(max_length=200, blank=True, null=True)
    api_token_key = models.CharField(max_length=200, blank=True, null=True)
    lastupdate = models.DateTimeField(db_column='LastUpdate',auto_now_add=True)  # Field name made lowercase.
    def __unicode__(self):
		return str(self.insurance_office)
    class Meta:
        managed = True
        db_table = 'insurace_office_registration'


class InsurancePremiumModelling(models.Model):
    #id = models.IntegerField(blank=True, null=True)
    hospital_id = models.IntegerField(blank=True, null=True)
    subject_id = models.IntegerField(blank=True, null=True)
    insurance_policy_id = models.IntegerField(blank=True, null=True)
    projected_premium = models.FloatField(blank=True, null=True)
    lastupdate = models.DateTimeField(db_column='LastUpdate',auto_now_add=True)  # Field name made lowercase.
    def __unicode__(self):
		return str(self.hospital_id)
    class Meta:
        managed = True
        db_table = 'insurance_premium_modelling'


class Insuranceplancategory(models.Model):
    insuranceplancategoryname = models.CharField(db_column='InsurancePlanCategoryName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    insuranceplancategorydocumention = models.TextField(db_column='InsurancePlanCategoryDocumention', blank=True, null=True)  # Field name made lowercase.
    lastupdate = models.DateTimeField(db_column='LastUpdate',auto_now_add=True)  # Field name made lowercase.
    def __unicode__(self):
		return str(self.insuranceplancategoryname)
    class Meta:
        managed = True
        db_table = 'insuranceplancategory'


# class PreminumModel(models.Model):
#     contactid = models.AutoField(db_column='ContactID')  # Field name made lowercase.
#     hospitalid = models.IntegerField(db_column='HospitalID', blank=True, null=True)  # Field name made lowercase.
#     subjectid = models.IntegerField(db_column='SubjectID', blank=True, null=True)  # Field name made lowercase.
#     sensorbasedscore = models.FloatField(db_column='SensorBasedScore', blank=True, null=True)  # Field name made lowercase.
#     laspseratio = models.FloatField(db_column='LaspseRatio', blank=True, null=True)  # Field name made lowercase.
#     age = models.FloatField(db_column='Age', blank=True, null=True)  # Field name made lowercase.
#     locationofstay = models.CharField(db_column='LocationofStay', max_length=111, blank=True, null=True)  # Field name made lowercase.
#     tobaccouse = models.IntegerField(db_column='TobaccoUse', blank=True, null=True)  # Field name made lowercase.
#     isindividualenrollement = models.IntegerField(db_column='IsIndividualEnrollement', blank=True, null=True)  # Field name made lowercase.
#     insuranceplancategoryid = models.IntegerField(db_column='InsurancePlanCategoryID', blank=True, null=True)  # Field name made lowercase.
#     bmi = models.FloatField(db_column='BMI', blank=True, null=True)  # Field name made lowercase.
#     gender = models.CharField(db_column='Gender', max_length=6, blank=True, null=True,choices=constant.Genders,default=constant.Genders.Male)  # Field name made lowercase.
#     maritalstatus = models.CharField(db_column='MaritalStatus', max_length=7, blank=True, null=True,choices=constant.MaritalStatus,default=constant.MaritalStatus.Single)  # Field name made lowercase.
#     profession = models.CharField(db_column='Profession', max_length=9, blank=True, null=True,choices=constant.Profession,default=constant.Profession.Normal)  # Field name made lowercase.
#     familysize = models.CharField(db_column='FamilySize', max_length=1, blank=True, null=True,choices=constant.FamilySize)  # Field name made lowercase.
#     medicalhistory = models.CharField(db_column='MedicalHistory', max_length=7, blank=True, null=True,choices=constant.MedicalHistory)  # Field name made lowercase.
#     lastupdate = models.DateTimeField(db_column='LastUpdate',auto_now_add=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = True
#         db_table = 'preminum_model'


class PublishSubscribeContact(models.Model):
    hospital_subject_device_id = models.ForeignKey('HospitalSubjectDeviceRegistration', models.DO_NOTHING, blank=True, null=True)
    InsuraceOfficeid =  models.ForeignKey('InsuraceOfficeRegistration', models.DO_NOTHING, blank=True, null=True)
    datastreamidentifier = models.CharField(db_column='DataStreamIdentifier', max_length=300)  # Field name made lowercase.
    documentation = models.TextField(db_column='Documentation')  # Field name made lowercase.
    startcollect = models.IntegerField(db_column='StartCollect', blank=True, null=True)  # Field name made lowercase.
    dateofcreation = models.DateTimeField(db_column='DateofCreation')  # Field name made lowercase.
    createbyid = models.IntegerField(db_column='CreateByID', blank=True, null=True)  # Field name made lowercase.
    intervalofpull = models.FloatField(db_column='IntervalofPull', blank=True, null=True)  # Field name made lowercase.
    lastupdate = models.DateTimeField(db_column='LastUpdate',auto_now_add=True)  # Field name made lowercase.
    class Meta:
        managed = True
        db_table = 'publish_subscribe_contact'


class SensorDeviceType(models.Model):
    devicename = models.CharField(max_length=200, blank=True, null=True)
    devicefunction = models.CharField(max_length=200, blank=True, null=True)
    measurement_unit = models.CharField(max_length=50, blank=True, null=True)
    documentation = models.CharField(max_length=400, blank=True, null=True)
    lastupdate = models.DateTimeField(db_column='LastUpdate',auto_now_add=True)  # Field name made lowercase.
    def __unicode__(self):
		return str(self.devicename)
    class Meta:
        managed = True
        db_table = 'sensor_device_type'

class Post(models.Model):
    author = models.ForeignKey(User)
    text = models.TextField()

    # Time is a rhinocerous
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']

    def __unicode__(self):
        return self.text+' - '+self.author.username




