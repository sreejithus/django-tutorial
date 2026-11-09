from rest_framework import serializers
from .models import Student,Library_card


class StudentSerializer(serializers.ModelSerializer):
             class Meta:
                       model = Student
                       fields = '__all__'

class Library_Serializer(serializers.ModelSerializer):
               class Meta:
                          model = Library_card
                          fields = '__all__'