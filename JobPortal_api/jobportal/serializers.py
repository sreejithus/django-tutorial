from rest_framework import serializers

from django.contrib.auth.models import User
from jobportal.models import Job


class UserSerializer(serializers.ModelSerializer):
                   class Meta:
                             model = User
                             fields  =['first_name','last_name','username','password','email']

                   def create(self, validated_data):
                            return User.objects.create_user(**validated_data)

class Jobserializer(serializers.ModelSerializer):
                    class Meta:
                               model = Job
                               fields  ='__all__'
                               read_only_fields = ['posted_by']
