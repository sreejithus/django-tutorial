from django.db import models
from  accounts.models import CustomUserModel
from events.models import Event
# Create your models her
from datetime import datetime,timedelta
class Booking(models.Model):
                      event = models.ForeignKey(Event,on_delete=models.CASCADE)
                      user = models.ForeignKey(CustomUserModel,on_delete=models.CASCADE)
                      seats = models.IntegerField()
                      amount = models.IntegerField()
                      status_choice =[
                              ("pending","pending"),
                              ("expired","expired"),
                              ("cancelled","cancelled"),
                              ("confirmed","confirmed")
                      ]
                      status = models.CharField(max_length=50,choices=status_choice,default="pending")
                      ticket_code = models.CharField(max_length=15,unique=True,null=True,blank=True)
                      created_at = models.DateTimeField(auto_now_add=True)
                      def check_expiration(self):
                                        booking_time =  self.created_at+timedelta(minutes=15)
                                        if datetime.now()>booking_time:
                                                     self.status = "expired"
                                                     self.save()
                                        return
                      
                                 