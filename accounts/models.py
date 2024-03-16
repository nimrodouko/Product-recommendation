from django.contrib.auth.models import AbstractUser
from django.db import models



class CustomUser(AbstractUser):
    gender = models.CharField(max_length=6, null=False,blank=False)
    budget = models.IntegerField(null=False, default=0, blank=False)
    age = models.PositiveIntegerField(null=False, blank=False,default=18)