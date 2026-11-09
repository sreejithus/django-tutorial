from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

# Create your views here.
from .models import Employee,Department
from .serializers import Userserializer,DepartmentSerializer,EmployeeSerializer,DepartmentEmployeeSerializer
from rest_framework import generics,viewsets,status
from rest_framework.permissions import IsAuthenticated
from .permissions import Isadmin
class Register(generics.CreateAPIView,generics.GenericAPIView):
           queryset = User.objects.all()
           serializer_class = Userserializer  

class EmployeeCrud(viewsets.ModelViewSet):
               permission_classes = [Isadmin]
               queryset = Employee.objects.all()
               serializer_class = EmployeeSerializer


class DepartmentCrud(viewsets.ModelViewSet):
             permission_classes=[Isadmin]
             queryset = Department.objects.all()
             serializer_class= DepartmentSerializer

class Department_Employee_view(APIView):
                permission_classes=[Isadmin]
                def get(self,request,id):
                             data =  get_object_or_404(Department,id=id)
                             serializer_instance =  DepartmentEmployeeSerializer(data)
                             return Response(serializer_instance.data ,status=status.HTTP_200_OK)
              
              
            


