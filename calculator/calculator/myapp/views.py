from django.shortcuts import render
from django.views import View
# Create your views here.



class Home(View):
      def get(self,request):
           return render(request,'home.html')


class Add(View):
      def get(self,request):
            return render(request,'add.html')

      def post(self,request):
            data = request.POST

            num1= data['number1']
            num2=data['number2']
            sum=int(num1)+int(num2)
            print(sum)

            context= {'sum':sum}
            return render(request,'add.html',context)
import math
class Factorial(View):
       def get(self,request):
                  return render(request,'factorial.html')
      
       def post(self,request):
                  data = request.POST
      
                  num1= int(data['number1'])
                  factorial = math.factorial(num1)
                  context ={
                         'factorial':factorial
                  }
                
      
                 
                  return render(request,'factorial.html',context)



class Bmi(View):
      def get(self,request):
            return render(request,'bmi.html')

      def post(self,request):
            data = request.POST

            h=int( data['height'])
            w=int(data['weight'])
            bmi = (w/((h/100)**2))
           

            context= {'bmi':bmi}
            return render(request,'bmi.html',context)