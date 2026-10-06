from django.shortcuts import render

# Create your views here.
from django.views import View
from django.http import HttpResponse,JsonResponse
from .models import Employee

from rest_framework.views import APIView
from rest_framework.response import Response

from django.shortcuts import get_object_or_404
from .serializers import Employee_Serializer
from rest_framework import status

#
class Employeelist(APIView):
    def get(self,request):
        qs=Employee.objects.all()
        #read all employee records from employee table
        serializer_instance = Employee_Serializer(qs,many=True)
        #Employee_serializer converts qs into python native types
        #qs contains more than one record so we use many = true
     
    
        return Response(data=serializer_instance.data)
        
          #send python natives data as json using response class



#API view for creating a new student record
# from json import loads
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
# @method_decorator(csrf_exempt,name="dispatch")
class Employeecreate(APIView):
    def post(self,request):

        serializer_instance = Employee_Serializer(data=request.data)
        if serializer_instance.is_valid():
        
            serializer_instance.save()
            return Response(serializer_instance.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)
                    
        
       

class Employeedetail(APIView):
    def get(self,request,i):
        # qs=Employee.objects.get(empid=i)
          e= get_object_or_404(Employee,empid=i)

          serializer_instance = Employee_Serializer(e)

       
          return Response(data=serializer_instance.data)
          
        


class Employeedelete(APIView):
    def delete(self,request,i):

        s=Employee.objects.get(empid=i)
    
        s.delete()
        return Response({"message":"Deleted Successfully"})


import json

class Employeefullupdate(APIView):
    def put(self,request,i):
         qs=Employee.objects.get(empid=i)
         serializer_instance = Employee_Serializer(qs,data=request.data)    
       
        
         if serializer_instance.is_valid():
                  serializer_instance.save()
                  return Response(serializer_instance.data)
         else:
              return Response(serializer_instance.errors)
                    
            

                         

       
      
        



class Employeepartalupdate(APIView):
     def patch(self,request,i):
                 qs=get_object_or_404(Employee,empid=i)
                 serializer_instance = Employee_Serializer(qs,data=request.data,partial=True)    
               
                
                 if serializer_instance.is_valid():
                          serializer_instance.save()
                          return Response(serializer_instance.data)
                 else:
                    return Response(serializer_instance.errors)
       