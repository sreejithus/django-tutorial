from django.db import models

# Create your models here

class Book(models.Model):
          title = models.CharField(max_length=100)
          author = models.CharField(max_length=100)
          language = models.CharField(max_length=100)
          price = models.IntegerField()
          pages = models.IntegerField()
          image = models.ImageField(upload_to='books',null=True)
