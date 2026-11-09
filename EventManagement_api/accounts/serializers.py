

from rest_framework import serializers
from accounts.models import CustomUserModel
class CustomUserSerializer(serializers.ModelSerializer):
              class Meta:
                         model= CustomUserModel
                         fields = ['id','username','password','email','first_name','last_name','role','phone']
                         read_only_fields =  ['id',]

              def create(self, validated_data):
                      return CustomUserModel.objects.create_user(**validated_data)