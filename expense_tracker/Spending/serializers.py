from rest_framework import serializers

from .models import Expense
from django.contrib.auth.models import User
class Userserializer(serializers.ModelSerializer):
             class Meta:
                      model= User
                      fields = ['first_name','last_name','username','password','email'] 
             def create(self, validated_data):
                     return User.objects.create_user(**validated_data)


class ExpenseSerializer(serializers.ModelSerializer):
                class Meta:
                         model = Expense
                         fields = '__all__'
                         read_only_fields = ['created_at','updated_at','owner','id']