from django.contrib.auth.models import AbstractUser
from django.db import models



class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, null=False,blank=False)
    MALE = 'Male'
    FEMALE ='Female'
    
    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        
    ]
    gender = models.CharField(null=False,blank=False,choices=GENDER_CHOICES,max_length=6)
    budget = models.IntegerField(null=False, default=0, blank=False)
    age = models.PositiveIntegerField(null=False, blank=False,default=18)