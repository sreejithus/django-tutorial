from django.db import models

# Create your models here.

from django.contrib.auth.models import User
class Department(models.Model):
         depname= models.CharField(max_length=100)
         depthead = models.CharField(max_length=100)
         

class Employee(models.Model):
           empid = models.IntegerField()
           name = models.CharField(max_length=100)
           designation  = models.CharField(max_length=100)
           department =  models.ForeignKey(Department,on_delete=models.CASCADE)
           salary =  models.IntegerField()
           
            





  