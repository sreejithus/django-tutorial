from django.db import models
from accounts.models import CustomUserModel
# Create your models here.
class Event(models.Model):
              title =  models.CharField(max_length=100)
              description   = models.TextField()
              date = models.DateField()
              time  = models.TimeField()
              venue = models.CharField(max_length=100)
              organizer = models.ForeignKey(CustomUserModel,on_delete=models.CASCADE)
              total_seats = models.IntegerField()
              available_seats = models.IntegerField()
              amount = models.IntegerField()
              created_at = models.DateTimeField(auto_now_add=True)
