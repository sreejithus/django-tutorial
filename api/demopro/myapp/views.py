from django.shortcuts import render
from django.views import View
from django.http import HttpResponse,JsonResponse


# Create your views here.





class Goodmorning(View):
       def get(self,request):
               data={
                       "message":"Good Morning"
               }
               return JsonResponse(data)



class Helloworld(View):
       def get(self,request):
             data={
                                    "message":"Hello World"
                            }
             return JsonResponse(data)

    
class Goodevening(View):
       def get(self,request):
               data={
                                      "message":"Good Evening"
                              }
               return JsonResponse(data)


class Userdetails(View):
        def get(self,request):

               data= [
                      {'name':"arun",'age':22,'place':"ekm"},
                      {'name':"arunima",'age':23,'place':"tvm"},
                      {'name':"joyal",'age':21,'place':"ekm"}
               ]
               return JsonResponse(data,safe=False)
from .models import Student


class Studentlist(View):
         def get(self,request):
                 data = list(Student.objects.all().values()) #convert list of dictionaries
                 print(data)
                
                

                 return JsonResponse(data,safe=False)


# from .models import Student

# class Addstudent(View):
#           def get(self,request):
#                   return render(request,'addstudent.html')
#           def post(self,request):
#                     data = request.POST
#                     rn= data['rollno']
#                     n= data['name']
#                     a=data['age']
#                     p=data['place']
#                     m=data['marks']
#                     S= Student.objects.create(rollnumber=rn,name=n,age=a,place=p,marks=m)
#                     S.save()
#                     return render(request,'addstudent.html')

from json import loads
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt 

@method_decorator(csrf_exempt,name='dispatch')
class Addstudent(View):
        def post(self,request):
                data= loads(request.body)#converts json into python native types
                r= data['rollnumber']
                n= data['name']
                a=data['age']
                p=data['place']
                m=data['marks']
                S= Student.objects.create(rollnumber=r,name=n,age=a,place=p,marks=m)
                S.save()

                return JsonResponse({"message":"Inserted Data sucessfully"})


#specific record reading

class StudentDetail(View):
        def get(self,request,i):
                s = list(Student.objects.filter(id=i).values())

                if s:
                        return JsonResponse(s,safe=False)
                else:
                        return JsonResponse({'message':"No Student Data"}) 
                
@method_decorator(csrf_exempt,name='dispatch')
class StudentDelete(View):
        def delete(self,request,i):
                 s=Student.objects.get(id=i)
                 s.delete()
                 return JsonResponse({"message":"deleted succesfullly"})

@method_decorator(csrf_exempt,name='dispatch')
class StudentFullUpdate(View):
        def put(self,request,i):
          
                data = loads(request.body)
                s= Student.objects.get(id=i)
                s.rollnumber= data['rollnumber']
                s.name= data['name']
                s.age=data['age']
                s.place=data['place']
                s.marks=data['marks']
                s.save()
        
                return JsonResponse({'message':"Data updated"}) 
@method_decorator(csrf_exempt,name='dispatch')
class StudentPartialUpdate(View):
          def patch(self,request,i):
                  data = loads(request.body)
                  print(data)
                  try:  
                        s= Student.objects.get(id=i)
                        if 'rollnumber' in data: 
                                         s.rollnumber= data['rollnumber']
                        if 'name' in data:
                                         s.name= data['name']
                        if 'age' in data:
                                         s.age=data['age']
                        if 'place' in data:
                                         s.place=data['place']
                        if 'marks' in data:
                                         s.marks = data['marks']
                  
                
                        s.save()
                        return JsonResponse({'message':"Data updated"}) 

                  except:
                        
                        return JsonResponse({'message':"No student Data"}) 
                          


