from django.db import models

# Create your models here.

class Movie(models.Model):
         
         title = models.CharField(max_length=100)
         director = models.CharField(max_length=100)
         language = models.CharField(max_length=100)
         year = models.IntegerField()
         rating = models.FloatField()
         runtime = models.FloatField()
         image = models.ImageField(upload_to='movies',null=True)



from django.contrib.auth.models import AbstractUser
class MyUser(AbstractUser):
          phone =  models.CharField(max_length=12,null=True)
          address= models.CharField(max_length=50,null=True)

            