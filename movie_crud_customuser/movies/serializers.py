

from rest_framework import serializers
from . models import Movie
# class Movie_Serializer(serializers.Serializer):
#                     title =serializers.CharField(max_length=100)
#                     director = serializers.CharField(max_length=100)
#                     language = serializers.CharField(max_length=100)
#                     year = serializers.IntegerField()
#                     rating = serializers.FloatField()
#                     runtime = serializers.FloatField()


#                     def create(self,validated_data):
#                               e  =  Movie.objects.create(**validated_data)
#                               return e
#                     def update(self,instance,validated_data):
#                                 instance.title = validated_data.get('title',instance.title)
#                                 instance.director = validated_data.get('director', instance.director)
#                                 instance.language = validated_data.get('language', instance.language)
#                                 instance.year = validated_data.get('year', instance.year)
#                                 instance.rating = validated_data.get('rating', instance.rating)
#                                 instance.runtime = validated_data.get('runtime', instance.runtime)
#                                 instance.save()
#                                 return instance


class Movie_Serializer(serializers.ModelSerializer):
           class Meta:
                   model=Movie
                   fields='__all__'
                    #or
                    # fields=['title','director','year',...]

           def validate(self,data):
                   if data['rating']>10 and data['rating']<0:
                           raise serializers.ValidationError({"message":"Invalid rating"})
                   return data

#to create user account we use user.objects.create_user() not user.objects.create()
#for password  hashing 
from . models import MyUser           
from django.contrib.auth.models import User 

from django.core.mail import send_mail
#send_mail(subject,message,from,to,fail_silently=True)
class UserSerializer(serializers.ModelSerializer):
            class Meta:
                    model = MyUser
                    fields = ['username','password','email','first_name','last_name','phone','address']
            def create(self,validated_data):
                                    u =  MyUser.objects.create_user(**validated_data) 
                                    send_mail("User Registration Confirmation Mail","Your account sucessfully created","sreejithus005@gmail.com",[u.email,],fail_silently=True)
                                    return u




            