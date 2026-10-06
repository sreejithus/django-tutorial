from django.shortcuts import render

# Create your views here.


from . models import Recipe
from . serializers import Recipe_serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404


class Recipe_list(APIView):
           def get(self,request):
                     qs =  Recipe.objects.all()

                     serializer_instance   =  Recipe_serializer(qs,many=True)

                     return Response(serializer_instance.data,status=status.HTTP_200_OK)


class Recipe_create(APIView):
         def post(self,request):
                     serializer_instance = Recipe_serializer(data = request.data)
                     if serializer_instance.is_valid():
                                                  serializer_instance.save()
                                                  return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
                     else:
                                                 return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)

class Recipe_retrive(APIView):
             def get(self,request,id):
                       r = get_object_or_404(Recipe,id=id)
                       serializer_instance =  Recipe_serializer(r)
                       return Response(serializer_instance.data,status=status.HTTP_200_OK)

class Recipe_full_update(APIView):
             def put(self,request,id):
                      r = get_object_or_404(Recipe,id=id)
                      serializer_instance =  Recipe_serializer(r,data = request.data)
                      if serializer_instance.is_valid():
                              serializer_instance.save()
                              return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
                      else:
                              return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)

class Recipe_partial_update(APIView):
             def patch(self,request,id):
                      r = get_object_or_404(Recipe,id=id)
                      serializer_instance =  Recipe_serializer(r,data = request.data,partial =True)
                      if serializer_instance.is_valid():
                              serializer_instance.save()
                              return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
                      else:
                              return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)


class Recipe_delete(APIView):
        def delete(self,request,id):
                     r = get_object_or_404(Recipe,id=id)
                     r.delete()
                     return Response({"message":"deleted successfully"},status=status.HTTP_204_NO_CONTENT)