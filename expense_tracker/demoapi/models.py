from django.db import models

# Create your models here.



class Student(models.Model):
                 name =  models.CharField(max_length=100)
                 department = models.CharField(max_length=50)

class Library_card(models.Model):
                  student = models.OneToOneField(Student,on_delete=models.CASCADE)
                  card_number = models.IntegerField()
                  created_at = models.DateTimeField(auto_now_add=True)