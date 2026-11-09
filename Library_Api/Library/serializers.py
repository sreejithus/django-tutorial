from .models import Book
from django.contrib.auth.models import User

from rest_framework import serializers

class Book_serializer(serializers.ModelSerializer):
            class Meta:
                 model = Book
                 fields = '__all__'


class User_Serializer(serializers.ModelSerializer):
           class Meta:
                   model= User
                   fields = ['username','password','first_name','last_name','email']

           def create(self,validated_data):
                     return User.objects.create_user(**validated_data)
