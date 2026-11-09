from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from  .models import Movie

from .serializers import Movie_Serializer
from django.shortcuts import get_object_or_404

from rest_framework import status
# class Movielist(APIView):


#     def get(self,request):
#            e  = Movie.objects.all()

#            serializer_instance = Movie_Serializer(e,many=True)

#            return Response(serializer_instance.data)


# class CreateMovie(APIView):
#                 def post(self,request):
#                            serializer_instance  =  Movie_Serializer(data=request.data)

#                            if serializer_instance.is_valid():
#                                     #  data after validation
#                                     #  cleaned_data =serializer_instance.validated_data
#                                     #  title = cleaned_data['title']
#                                      serializer_instance.save()
#                                      return Response(serializer_instance.data)
#                            else:
#                                    return Response(serializer_instance.errors)
                           

class Moviecreatelist(APIView):
           def get(self,request):
                      e  = Movie.objects.all()

                      serializer_instance = Movie_Serializer(e,many=True)

                      return Response(serializer_instance.data,status=status.HTTP_200_OK)
           def post(self,request):
                           serializer_instance  =  Movie_Serializer(data=request.data)

                           if serializer_instance.is_valid():
                                    #  data after validation
                                    #  cleaned_data =serializer_instance.validated_data
                                    #  title = cleaned_data['title']
                                     serializer_instance.save()
                                     return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
                           else:
                                   return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)



class Retriveupdatedelete(APIView):
             def get(self,request,i):
                     e = get_object_or_404(Movie,id=i)
                     serializer_instance = Movie_Serializer(e)
                     return Response(serializer_instance.data,status=status.HTTP_200_OK) 
             def put(self,request,i):
                     m = get_object_or_404(Movie,id=i)
                     serilaizer_instance = Movie_Serializer(m,data=request.data)
                     if serilaizer_instance.is_valid():
                             serilaizer_instance.save()
                             return  Response(serilaizer_instance.data,status=status.HTTP_201_CREATED)
                     else: 
                            return Response(serilaizer_instance.errors,status=status.HTTP_400_BAD_REQUEST)

             def patch(self,request,i):
                        m = get_object_or_404(Movie,id=i)
                        serilaizer_instance = Movie_Serializer(m,data=request.data,partial=True)
                        if serilaizer_instance.is_valid():
                                 serilaizer_instance.save()
                                 return Response(serilaizer_instance.data,status=status.HTTP_201_CREATED)
                        else: 
                              return Response(serilaizer_instance.errors,status.HTTP_400_BAD_REQUEST)

             def delete(self,request,i):
                          d=get_object_or_404(Movie,id=i)
                          d.delete()
                          return Response({"message":"deleted sucessfully"},status =status.HTTP_204_NO_CONTENTt)



                     
                         
                             


            

