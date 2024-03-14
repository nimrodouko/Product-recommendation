from django.contrib.auth.models import AbstractUser
from django.db import models



class CustomUser(AbstractUser):
    gender = models.CharField(max_length=6)
    budget = models.IntegerField()
    age = models.PositiveIntegerField()