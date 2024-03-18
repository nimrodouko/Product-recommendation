from django.contrib.auth.models import AbstractUser
from django.db import models



class CustomUser(AbstractUser):
    MALE = 'Male'
    FEMALE ='Female'
    RURAL ='Rural'
    URBAN = 'Urban'
    
    LOCATION =[
        (RURAL,'Rural'),
        (URBAN, 'Urban')
    ]
    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        
    ]
    gender = models.CharField(max_length=6, null=False,blank=False,choices=GENDER_CHOICES)
    
    budget = models.IntegerField(null=False, default=0, blank=False)
    age = models.PositiveIntegerField(null=False, blank=False,default=18)
    location = models.CharField(max_length=5,null=False,blank=False,choices=LOCATION)