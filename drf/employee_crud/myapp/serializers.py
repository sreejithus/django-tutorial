from rest_framework import serializers


from .models import Employee
class Employee_Serializer(serializers.Serializer):
          empid = serializers.IntegerField()
          name = serializers.CharField(max_length=100)
          age = serializers.IntegerField()
          salary  = serializers.IntegerField()
          join_date = serializers.DateField()
          gender_choices = [
                              ('m' ,'male'),
                              ('f','female')
                     ]
          gender = serializers.ChoiceField(choices=gender_choices)
          designation = serializers.CharField(max_length=100)
          profile_img = serializers.ImageField()

          def create(self,validated_data):
                     s = Employee.objects.create(**validated_data)
                     return s

          def update(self, instance, validated_data):
                      instance.empid = validated_data.get('empid', instance.empid)
                      instance.name = validated_data.get('name', instance.name)
                      instance.age = validated_data.get('age', instance.age)
                      instance.salary = validated_data.get('salary', instance.salary)
                      instance.join_date = validated_data.get('join_date', instance.join_date)
                      instance.gender = validated_data.get('gender', instance.gender)
                      instance.designation = validated_data.get('designation', instance.designation)
                      instance.save()
                      return instance
          def validate(self,data):
                     if data['age']<0:
                             raise serializers.ValidationError("age must be positive")
                     return data