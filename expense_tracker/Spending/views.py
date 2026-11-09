from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework import status
from .models import Expense
from .serializers import Userserializer,ExpenseSerializer
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from .permissions import Isowner
class Register_user(APIView):
            def post(self,request):
                           serializer_instance = Userserializer(data=request.data)
                           if serializer_instance.is_valid():
                                       serializer_instance.save()
                                       return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
                           else:
                                   Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)



class Current_Loggedin(APIView):
                permission_classes= [IsAuthenticated]
                def get(self,request):
                        
                            u = request.user
                            serializer_instance  = Userserializer(u)
        
                            return Response(serializer_instance.data,status=status.HTTP_200_OK)

class ExpenseCreate(APIView):
            permission_classes=[IsAuthenticated]
            
            def post(self,request):
                         form_data =  request.data
                         serializer_instance  = ExpenseSerializer(data=form_data)
                         if serializer_instance.is_valid():
                                   serializer_instance.save(owner=request.user)
                                   return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
                         else:
                                  return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)

class ExpenseList(APIView):
               permission_classes = [IsAuthenticated]
               def get(self,request):
                             queryset = Expense.objects.filter(owner=request.user.id)
                             serializer_instance = ExpenseSerializer(queryset,many=True)
                             return Response(serializer_instance.data,status=status.HTTP_200_OK)


class ExpenseRetrive(APIView):
                permission_classes = [IsAuthenticated,Isowner]
                def get(self,request,id):
                               u = get_object_or_404(Expense,id=id)
                               self.check_object_permissions(request,u)
                               serializer_instance = ExpenseSerializer(u)
                               return Response(serializer_instance.data,status=status.HTTP_200_OK)


class UpdateExpense(APIView):
              permission_classes = [IsAuthenticated,Isowner]
              def put(self,request,id):
                               u = get_object_or_404(Expense,id=id)
                               self.check_object_permissions(request,u)
                               serializer_instance = ExpenseSerializer(u,data=request.data)

                               if serializer_instance.is_valid():
                                          serializer_instance.save()
                                          return Response(serializer_instance.data,status= status.HTTP_200_OK)
                               else:
                                       return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)

class DeleteExpense(APIView):
                    permission_classes = [IsAuthenticated,Isowner]
                    def delete(self,request,id):
                                u = get_object_or_404(Expense,id=id)
                                self.check_object_permissions(request,u)
                                u.delete()
                                return Response(status=status.HTTP_204_NO_CONTENT)


from datetime import datetime 
from django.db.models import Sum                  
class ExpenseSummery(APIView):
                permission_classes = [IsAuthenticated,Isowner]
                def get(self,request):
                            today = datetime.now().date()
                            qs =  Expense.objects.filter(owner =request.user,created_at=today)
                            response_data =  {
                                                 'today_total' : 0,
                                                 'monthly_total':0
                            }
                            if qs:
                                    
                                      today_expense =qs.aggregate(total = Sum('amount')) 
                                      total = today_expense.get('total')
                                
                         

                                      category_summery  = qs.values('category').annotate(total = Sum('amount'))
                                     
                                      response_data['today_total'] = total
                                      response_data['category_total_today']= category_summery
                            
                           
                            month = datetime.now().date().month
                            year = datetime.now().date().year
                                                                    
                            qs =  Expense.objects.filter(owner =request.user,created_at__month=month,created_at__year=year)
                            
                            if qs:
                                                                            
                                                                              monthly_expense =qs.aggregate(total = Sum('amount')) 
                                                                              monthly_expense_total = monthly_expense.get('total')
                                                                        
                                                                 
                                        
                                                                              category_summery  = qs.values('category').annotate(total = Sum('amount'))
                                                                              response_data['monthly_total'] = monthly_expense_total
                                                                              response_data['category_total_month']= category_summery
                                                                              
                                                                    
                            return Response(response_data)  
                        
from . import ai_integration
class ExpenseBudgetPlan(APIView):
                    def get(self,request):
                               response_data = {
                                       'monthly_expense':0
                               }
                               month = datetime.now().date().month
                               year = datetime.now().date().year
                                                                                                   
                               qs =  Expense.objects.filter(owner =request.user,created_at__month=month,created_at__year=year)
                                                           
                               if qs:
                                                                                                           
                                                                                                             monthly_expense =qs.aggregate(total = Sum('amount')) 
                                                                                                             monthly_expense_total = monthly_expense.get('total')
                                                                                                       
                                                                                                
                                                                       
                                                                                                             category_summery  = qs.values('category').annotate(total = Sum('amount'))
                                                                                                             response_data['monthly_expense'] = monthly_expense_total
                                                                                                             response_data['category_expense_month']= category_summery

                               ai_integration.get_budget_plan(response_data)                                                      
                                                                                                   
                               return Response(response_data)  
                                        