from django.db import models

# Create your models here.


class Person(models.Model):
       
         name=models.CharField(max_length=100)
         age=models.IntegerField()
         place=models.CharField(max_length=20)



         def __str__(self):
                      return self.name







class Movie(models.Model):
         movie_name = models.CharField(max_length=100)
         director= models.CharField(max_length=100)
         year= models.IntegerField()