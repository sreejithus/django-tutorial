from django.db.models.signals import post_save,post_delete

from .models import Booking
from django.dispatch import receiver


#uuid.uuid(4)
import uuid
@receiver(post_save,sender=Booking)
def update_after_status(sender,instance,created,**kwargs):
                     
                                 if instance.status == "confirmed" and not(instance.ticket_code):
                                                code =f" Tick-{uuid.uuid4().hex[:8]}"
                                                instance.ticket_code = code
                                                event = instance.event
                                                event.available_seats -=instance.seats 
                                                event.save(update_fields=['available_seats'])
                                                instance.save(update_fields = ['ticket_code'])
                                 elif instance.status =="cancelled":
                                                                            if instance.ticket_code:
                                                                                         event = instance.event
                                                                                         event.available_seats +=instance.seats 
                                                                                         event.save(update_fields = ['available_seats'])
                                                                                         instance.ticket_code =''
                                                                                         instance.save(update_fields =['ticket_code'])
                                                                        
                                                     
                                


@receiver(post_delete,sender=Booking)
def update_after_delete(sender,instance,**kwargs):
                     
                                 if instance.status == "confirmed" and instance.ticket_code:
                                                
                                                event = instance.event
                                                event.available_seats +=instance.seats 
                                                event.save(update_fields = ['available_seats'])
                               
