from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUserModel(AbstractUser):
                   role_choice = [
                           ('organizer','Organizer'),
                           ('customer','customer')
                   ]

                   role =  models.CharField(max_length=50,choices=role_choice)
                   phone = models.CharField(max_length=20)