from django.shortcuts import render

# Create your views here.
from accounts.models import CustomUserModel
from rest_framework.views import Response,APIView
from accounts.serializers import CustomUserSerializer
from rest_framework.permissions import IsAuthenticated

from rest_framework import status
class Register(APIView):
                def post(self,request):
                            form_data =  request.data
                            serializer_instance =  CustomUserSerializer(data = form_data)
                            if serializer_instance.is_valid():
                                          serializer_instance.save()
                                          return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
                            else:
                                    return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)
                            
class Logout(APIView):
                  permission_classes = [IsAuthenticated]
                  def post(self,request):
                            request.user.auth_token.delete()
                            return Response({"message":"logout sucessfully"},status=status.HTTP_200_OK)
