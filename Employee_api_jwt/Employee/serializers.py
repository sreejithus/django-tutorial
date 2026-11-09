from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Department,Employee

class Userserializer(serializers.ModelSerializer):
           class Meta:
                   model = User
                   fields=['first_name','last_name','username','password','email']
           def create(self, validated_data):
                    return User.objects.create_user(**validated_data)



class DepartmentSerializer(serializers.ModelSerializer):
           
            
            class Meta:
                   model = Department
                   fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
           department = DepartmentSerializer(read_only =True)
           class Meta:
                   model = Employee
                   fields= '__all__'

class DepartmentEmployeeSerializer(serializers.ModelSerializer):
            employee = EmployeeSerializer(source='employee_set',read_only = True,many=True)
            
            class Meta:
                   model = Department
                   fields = '__all__'

