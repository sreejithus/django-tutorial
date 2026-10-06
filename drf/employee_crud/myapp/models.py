from django.db import models

# Create your models here.




class Employee(models.Model):
          empid = models.IntegerField(unique=True)
          name = models.CharField(max_length=100)
          age = models.IntegerField()
          salary  = models.IntegerField()
          join_date = models.DateField()
          gender_choices = [
                              ('m' ,'male'),
                              ('f','female')
                     ]
          gender = models.CharField(max_length=100,choices=gender_choices)
          designation = models.CharField(max_length=100)
          profile_img = models.ImageField(upload_to='profiles',null=True)
         