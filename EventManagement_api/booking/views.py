from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

# Create your views here.


from django.shortcuts import render,get_object_or_404

# Create your view
from booking.models import Booking
from rest_framework.views import APIView
from rest_framework.response import Response
from booking.serializers import BookingSerializer
from rest_framework.permissions import IsAuthenticated
from booking.permissions import Iscustomer

from rest_framework import status
class CreateorList(APIView):
                permission_classes =[Iscustomer]
                def get(self,request):
                                        user = request.user
                                        if(user.role =='customer'):
                                                 qs =  Booking.objects.filter(user =request.user)
                                        else:
                                                 qs = Booking.objects.filter(event__organizer = request.user)
                                                

                                     
                                        serializer_instance  =  BookingSerializer(qs,many=True)
                                        return Response(serializer_instance.data,status=status.HTTP_200_OK)
                def post(self,request):
                            form_data =  request.data
                            serializer_instance =  BookingSerializer(data = form_data)
                            if serializer_instance.is_valid():
                                          data =  serializer_instance.validated_data
                                          event = data['event']
                                          seats = data['seats']
                                          amount = event.amount * seats
                                          serializer_instance.save(user = request.user, amount=amount)
                                          response =  {
                                                                                          "message":"""Booking successfully Created,payment is Pending, make your payment within 15 minutes""",
                                                                                          "booking_data":serializer_instance.data
                                                                                          
                                                                                  }
                                          
                                                                                  
                                          return Response(response,status=status.HTTP_201_CREATED)
                            else:
                                    return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)
class RetriveUpdateDelete(APIView):
                  permission_classes  =  [Iscustomer]
                  def get(self,request,id):
                                          obj  =  get_object_or_404(Booking,id=id)
                                          
                                          serializer_instance = BookingSerializer(obj)
                                          return Response(serializer_instance.data,status=status.HTTP_200_OK) 

                                            
                          
                  def put(self,request,id):
                                        obj  =  get_object_or_404(Booking,id=id)
                                        self.check_object_permissions(request,obj)
                                        serializer_instance = BookingSerializer(obj,data=request.data)
                                        if serializer_instance.is_valid():
                                                           serializer_instance.save(organizer = request.user)
                                                           return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
                                        else:
                                                return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)
                  def patch(self,request,id):
                                                            obj  =  get_object_or_404(Booking,id=id)
                                                            self.check_object_permissions(request,obj)
                                                            serializer_instance = BookingSerializer(obj,data=request.data,partial=True)
                                                            if serializer_instance.is_valid():
                                                                               serializer_instance.save()
                                                                               return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
                                                            else:
                                                                    return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)
                  def delete(self,request,id):
                                                                                obj  =  get_object_or_404(Booking,id=id)
                                                                                self.check_object_permissions(request,obj)
                                                                                obj.delete()
                                                                                return Response({"message":"deleted sucessfully"},status=status.HTTP_204_NO_CONTENT)
                                                                                
class Cancell_view(APIView):
                          permission_classes=[Iscustomer]
                          def get(self,request,id):
                                          obj = get_object_or_404(Booking,id=id)
                                          self.check_object_permissions(request,obj)
                                          obj.status = "cancelled"
                                          obj.save()
                                          
                                          return Response({"message":"booking sucessfully cancelled"},status=status.HTTP_200_OK)