from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from  .models import Movie

from .serializers import Movie_Serializer,UserSerializer
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
                           

# class Moviecreatelist(APIView):
#            def get(self,request):
#                       e  = Movie.objects.all()

#                       serializer_instance = Movie_Serializer(e,many=True)

#                       return Response(serializer_instance.data,status=status.HTTP_200_OK)
#            def post(self,request):
#                            serializer_instance  =  Movie_Serializer(data=request.data)

#                            if serializer_instance.is_valid():
#                                     #  data after validation
#                                     #  cleaned_data =serializer_instance.validated_data
#                                     #  title = cleaned_data['title']
#                                      serializer_instance.save()
#                                      return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
#                            else:
#                                    return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)



# class Retriveupdatedelete(APIView):
#              def get(self,request,i):
#                      e = get_object_or_404(Movie,id=i)
#                      serializer_instance = Movie_Serializer(e)
#                      return Response(serializer_instance.data,status=status.HTTP_200_OK) 
#              def put(self,request,i):
#                      m = get_object_or_404(Movie,id=i)
#                      serilaizer_instance = Movie_Serializer(m,data=request.data)
#                      if serilaizer_instance.is_valid():
#                              serilaizer_instance.save()
#                              return  Response(serilaizer_instance.data,status=status.HTTP_201_CREATED)
#                      else: 
#                             return Response(serilaizer_instance.errors,status=status.HTTP_400_BAD_REQUEST)

#              def patch(self,request,i):
#                         m = get_object_or_404(Movie,id=i)
#                         serilaizer_instance = Movie_Serializer(m,data=request.data,partial=True)
#                         if serilaizer_instance.is_valid():
#                                  serilaizer_instance.save()
#                                  return Response(serilaizer_instance.data,status=status.HTTP_201_CREATED)
#                         else: 
#                               return Response(serilaizer_instance.errors,status.HTTP_400_BAD_REQUEST)

#              def delete(self,request,i):
#                           d=get_object_or_404(Movie,id=i)
#                           d.delete()
#                           return Response({"message":"deleted sucessfully"},status =status.HTTP_204_NO_CONTENTt)


# from rest_framework import mixins,generics

# class Moviecreatelist(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
#            queryset = Movie.objects.all()
#            serializer_class = Movie_Serializer

#            def get(self,request):
#                     return self.list(request)
#            def post(self,request):
#                    return self.create(request)

# class Retriveupdatedelete(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
#              queryset = Movie.objects.all()
#              serializer_class = Movie_Serializer

#              def get(self,request,pk):
#                      return self.retrieve(request,pk)
#              def put(self,request,pk):
#                       return self.update(request,pk)
#              def patch(self,request,pk):
#                      return self.partial_update(request,pk)
#              def  delete(self,request,pk):
#                      return self.destroy(request,pk)
             
                             


            
from rest_framework import mixins,generics

# class Moviecreatelist(generics.ListCreateAPIView,generics.GenericAPIView):
#            serializer_class= Movie_Serializer
#            queryset = Movie.objects.all()

# class Retriveupdatedelete(generics.RetrieveUpdateDestroyAPIView,generics.GenericAPIView):
#              queryset = Movie.objects.all()
#              serializer_class = Movie_Serializer



from rest_framework import viewsets
from django.db.models import Q

from rest_framework.permissions import IsAuthenticated

class Movieview(viewsets.ModelViewSet):
              permission_classes=[IsAuthenticated]
              queryset = Movie.objects.all()
              serializer_class = Movie_Serializer


# class Moviesearch(APIView):
#           def get(self,request):
#                   data =  self.request.query_params.get('search')
#                   m  = Movie.objects.filter(Q(title__icontains =data )|Q(director__icontains = data)|Q(director__icontains = data))
#                   if not m.exists():
#                           return Response({"message":"no records found"},status=status.HTTP_200_OK)
#                   serializer_instance  =  Movie_Serializer(m,many= True)
#                   return Response(serializer_instance.data,status=status.HTTP_200_OK)


from rest_framework.filters import SearchFilter
class Moviesearch(generics.ListAPIView,generics.GenericAPIView):
                                queryset = Movie.objects.all()
                                serializer_class = Movie_Serializer
                                filter_backends = [SearchFilter]
                                search_fields = ['title','director']


from django.contrib.auth.models import User 
class Registeruser(APIView):

          def post(self,request):
                    form_data = request.data
                    serializer_instance =  UserSerializer(data =form_data)
                    if serializer_instance.is_valid():
                             serializer_instance.save()
                             return Response(serializer_instance.data,status= status.HTTP_201_CREATED)
                    else:
                            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)