from django.shortcuts import render

# Create your views here.
from django.views import View
from django.http import HttpResponse,JsonResponse
from .models import Employee
class Employeelist(View):
    def get(self,request):
        s=Employee.objects.all().values()
        print(s)
        print(type(s))
        data=list(s)
        print(data)
        print(type(data))
        return JsonResponse(data,safe=False)

#API view for creating a new student record
from json import loads
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
@method_decorator(csrf_exempt,name="dispatch")
class Employeecreate(View):
    def post(self,request):
        data=loads(request.body)
        e=data['empid']
        n=data['name']
        a=data['age']
        p=data['place']
        g=data['gender']
        sa=data['salary']
        d=data['designation']
        s=Employee.objects.create(empid=e,name=n,age=a,place=p,gender=g,salary=sa,deignation=d)
        # s = Employee.objects.create(**data)
        s.save()
        return JsonResponse({"message":"Inserted data successfully"})

class Employeedetail(View):
    def get(self,request,i):
        s=list(Employee.objects.filter(id=i).values())
        if s:
            return JsonResponse(s,safe=False)
        else:
            return JsonResponse({"message":"No employee data"})

@method_decorator(csrf_exempt,name="dispatch")
class Employeedelete(View):
    def delete(self,request,i):
        s=Employee.objects.get(id=i)
        s.delete()
        return JsonResponse({"message":"Deleted Successfully"})


import json

@method_decorator(csrf_exempt,name="dispatch")
class Employeefullupdate(View):
    def put(self,request,i):
        data = json.loads(request.body)
        print(data)

        s=Employee.objects.get(id=i)
        s.empid = data['empid']
        s.name =data['name']
        s.age = data['age']
        s.place = data['place']
        s.salary =data['salary']
        s.joindate= data['joindate']
        s.designation = data['designation']
        s.save()
        return JsonResponse({"message":"updated Successfully"})


@method_decorator(csrf_exempt,name="dispatch")
class Employeepartalupdate(View):
    def patch(self,request,i):
        data = json.loads(request.body)
        print(data)

        s=Employee.objects.get(id=i)
        if 'empid' in data :
            s.empid= data['empid']
        if 'name' in data:
            s.name =data['name']
        if 'age' in data:
            s.age = data['age']
        if 'place' in data:
            s.place = data['place']
        if 'salary' in data:
            s.salary =data['salary']
        if 'joindate' in data:
            s.joindate =data['joindate']
        if 'designation' in data:
            s.designation =data['designation']
        s.save()
        return JsonResponse({"message":"updated partally"})