from django.shortcuts import render
from rest_framework.views import APIView
from .models import Book
from .serializers import User_Serializer,Book_serializer
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
# Create your views here.

from rest_framework.permissions import AllowAny,IsAuthenticated


class ListCreate(APIView):
         permission_classes = [IsAuthenticated]
         
         def get(self,request):
                   
                   data = Book.objects.all()
                   serializer_instance = Book_serializer(data,many=True)
                   return Response(serializer_instance.data,status=status.HTTP_200_OK)


         def post(self,request):
                     
                     serializer_instance = Book_serializer(data=request.data)
                     if serializer_instance.is_valid():
                                               serializer_instance.save()
                                               return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
                   
                     else:
                             return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)
                   
                   

class RetrieveUpdateDelete(APIView):
          permission_classes = [IsAuthenticated]
          
          def get(self,request,id):
                   data = get_object_or_404(Book,id=id)
                   serializer_instance = Book_serializer(data)
                   return Response(serializer_instance.data,status=status.HTTP_200_OK)
          def put(self,request,id):
                   obj = get_object_or_404(Book,id=id)
                   serializer_instance= Book_serializer(obj,data=request.data)
                   if serializer_instance.is_valid():
                           serializer_instance.save()
                           return Response(serializer_instance.data,status=status.HTTP_200_OK)
                   else:
                           return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)
          def patch(self,request,id):
                            obj = get_object_or_404(Book,id=id)
                            serializer_instance= Book_serializer(obj,data=request.data,partial=True)
                            if serializer_instance.is_valid():
                                    serializer_instance.save()
                                    return Response(serializer_instance.data,status=status.HTTP_200_OK)
                            else:
                                    return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)
          def delete(self,request,id):
                            data=get_object_or_404(Book,id=id)
                            data.delete()
                            return Response(status=status.HTTP_204_NO_CONTENT)
         

class RegisterUser(APIView):
           def post(self,request):
                     serializer_instance = User_Serializer(data=request.data)
                     if serializer_instance.is_valid():
                             serializer_instance.save()
                             return Response(serializer_instance.data,status=status.HTTP_200_OK)
                     else:
                             return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)


class Logout(APIView):
          permission_classes=[IsAuthenticated]
          def post(self,request):
                      self.request.user.auth_token.delete()
                      return Response({"message": "Logout Successfully"}, status=status.HTTP_200_OK)

from rest_framework.filters import SearchFilter
from rest_framework import generics
class SearchItem(generics.ListAPIView):
          queryset=Book.objects.all()
          serializer_class= Book_serializer
          permission_classes=[IsAuthenticated]
          filter_backends=[SearchFilter]
          search_fields =['title','author','language']
          
                       