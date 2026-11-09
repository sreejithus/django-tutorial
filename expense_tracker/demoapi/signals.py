from .models import Student
from django.db.models.signals import post_delete,post_save
from django.dispatch import receiver
@receiver(post_save,sender=Student)
def fun1(sender,instance,created,**kwargs):
            if created:
                print("student record addeded")


@receiver(post_delete,sender=Student)
def fun1(sender,instance,created,**kwargs):
            print("student record deleted")
