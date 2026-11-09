from rest_framework import serializers
from Todo.models import Task 
from django.contrib.auth.models import User
class Task_serializer(serializers.ModelSerializer):
        class Meta:
                  model = Task
                  fields='__all__'
                  read_only_fields = ['user',]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','password','email','first_name','last_name']

    def create(self,validated_data):
        u=User.objects.create_user(**validated_data)
        u.save()
        return u
