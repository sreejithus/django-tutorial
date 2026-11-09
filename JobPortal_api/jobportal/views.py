from django.shortcuts import render
from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework import status
from .models import Job
from .serializers import UserSerializer,Jobserializer
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from .permissions import Isowner
# Create your views here.

from rest_framework.views import APIView




class Register(APIView):
                def post(self,request):
                                  serializer_instance =  UserSerializer(data=request.data)
                                  if serializer_instance.is_valid():
                                                  serializer_instance.save()
                                                  return Response(serializer_instance.data,status= status.HTTP_201_CREATED)
                                  else:
                                          return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)
class JObListandCreate(APIView):
                     permission_classes=[Isowner]
                     def get(self,request):
                                qs=  Job.objects.all()
                                serializer_instance =  Jobserializer(qs,many=True)
                                return Response(serializer_instance.data,status=status.HTTP_200_OK)
                     def post(self,request):
                                        serializer_instance =  Jobserializer(data=request.data)
                                        if serializer_instance.is_valid():
                                                  serializer_instance.save(posted_by =request.user)
                                                  return Response(serializer_instance.data,status= status.HTTP_201_CREATED)
                                        else:
                                                                                  return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)

class RetrieveUpdateDeleteJob(APIView):
                       permission_classes=[Isowner]
                       def get(self,request,id):
                                   obj = get_object_or_404(Job,id=id)
                                   self.check_object_permissions(request,obj)
                                   serializer_instance  = Jobserializer(obj)
                                   return Response(serializer_instance.data,status=status.HTTP_200_OK) 
                       def put(self,request,id):
                                      obj = get_object_or_404(Job,id=id)
                                      self.check_object_permissions(request,obj)
                                      serializer_instance  = Jobserializer(obj,data=request.data)
                                      if serializer_instance.is_valid():
                                                 serializer_instance.save()
                                                 return Response(serializer_instance.data,status= status.HTTP_200_OK)
                                      else:
                                                                                return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)
                       def delete(self,request,id):
                                     obj = get_object_or_404(Job,id=id)
                                     self.check_object_permissions(request,obj)
                                     obj.delete()
                                     return Response({"message":"deleted sucessfully"},status=status.HTTP_200_OK)
                                    
                                                 
                                      