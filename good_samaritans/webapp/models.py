from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BasicInfo(models.Model):
    '''
    Basic info for people, registered or not.

    '''
    phone_number = models.CharField(max_length=140)
    first_name = models.CharField(max_length=140)
    last_name = models.CharField(max_length=140)
    email = models.EmailField(max_length=140)


class UserProfile(models.Model):
    '''
    The base user profile class

    '''
    user = models.ForeignKey(User, unique=True)
    basic_info = models.ForeignKey(BasicInfo, unique=True)
    location_text = models.CharField(max_length=140)
    location_lat = models.FloatField()
    location_lon = models.FloatField()
    gender = models.CharField(max_length=10)
    imei = models.CharField(max_length=140)
    to_notify = models.ManyToManyField(BasicInfo, related_name='kin') 


class Notification(models.Model):
    content = models.CharField(max_length=400)
    owner = models.ForeignKey(UserProfile)


