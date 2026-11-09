from django.db import models

# Create your models here.


from django.contrib.auth.models import User

class Expense(models.Model):
             title = models.CharField(max_length=100)
             amount = models.IntegerField()
             category_chioces =[
                     ('food','Food'),
                     ('travel','Travel'),
                     ('bill','Bill'),
                     ('entertainment','Entertainment'),
                     ('others','Others')
                     
                                  ] 
             category = models.CharField(max_length=15,choices=category_chioces)
             priority_choices = [
                     ('need','Need'),

                     ('want','Want')
             ]

             priority = models.CharField(max_length=30,choices=priority_choices)
             payment_choices = [
                     ('upi','Upi'),
                     ('cash','Cash')
             ]

             payment = models.CharField(max_length=30,choices=payment_choices)
             created_at = models.DateField(auto_now_add=True)
             updated_at = models.DateField(auto_now=True)
             owner =  models.ForeignKey(User,on_delete=models.CASCADE,related_name='expenses')
