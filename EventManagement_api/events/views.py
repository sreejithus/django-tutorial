from django.shortcuts import render

# Create your views here.


from django.shortcuts import render,get_object_or_404

# Create your view
from events.models import Event
from rest_framework.views import APIView
from rest_framework.response import Response
from events.serializers import EventSerializer
from rest_framework.permissions import IsAuthenticated
from events.permissions import IsOrgainserOrReadonly

from rest_framework import status
class CreateorList(APIView):
                permission_classes =[IsOrgainserOrReadonly]
                def get(self,request):
                                        qs =  Event.objects.all()
                                        serializer_instance  =  EventSerializer(qs,many=True)
                                        return Response(serializer_instance.data,status=status.HTTP_200_OK)
                def post(self,request):
                            form_data =  request.data
                            serializer_instance =  EventSerializer(data = form_data)
                            if serializer_instance.is_valid():
                                          serializer_instance.save(organizer = request.user)
                                          return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
                            else:
                                    return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)
class RetriveUpdateDelete(APIView):
                  permission_classes  =  [IsOrgainserOrReadonly]
                  def get(self,request,id):
                                          obj  =  get_object_or_404(Event,id=id)
                                          
                                          serializer_instance = EventSerializer(obj)
                                          return Response(serializer_instance.data,status=status.HTTP_200_OK) 

                                            
                          
                  def put(self,request,id):
                                        obj  =  get_object_or_404(Event,id=id)
                                        self.check_object_permissions(request,obj)
                                        serializer_instance = EventSerializer(obj,data=request.data)
                                        if serializer_instance.is_valid():
                                                           serializer_instance.save(organizer = request.user)
                                                           return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
                                        else:
                                                return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)
                  def patch(self,request,id):
                                                            obj  =  get_object_or_404(Event,id=id)
                                                            self.check_object_permissions(request,obj)
                                                            serializer_instance = EventSerializer(obj,data=request.data,partial=True)
                                                            if serializer_instance.is_valid():
                                                                               serializer_instance.save()
                                                                               return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
                                                            else:
                                                                    return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)
                  def delete(self,request,id):
                                                                                obj  =  get_object_or_404(Event,id=id)
                                                                                self.check_object_permissions(request,obj)
                                                                                obj.delete()
                                                                                return Response({"message":"deleted sucessfully"},status=status.HTTP_204_NO_CONTENT)
                                                                                
                                                                     