from rest_framework import serializers
from events.models import Event

import datetime
class EventSerializer(serializers.ModelSerializer):
              class Meta:
                       model= Event
                       fields = "__all__"
                       read_only_fields = ['organizer','created_at']
              def validate(self, data):
                               today_date =  datetime.date.today()
                               event_date = data['date']
                               if today_date>event_date:
                                          raise serializers.ValidationError("invalid date ,choose an right date")
                               return data
