from django.shortcuts import render
from .serializers import UserSerializer,Task_serializer
from django.contrib.auth.models import User
from .models import Task
from .permissions import Isowner
from rest_framework.permissions import IsAuthenticated
# Create your views here.

from rest_framework import generics,viewsets
class TaskView(viewsets.ModelViewSet):
            queryset =  Task.objects.all()
            serializer_class =  Task_serializer
            permission_classes = [Isowner,IsAuthenticated]
            def perform_create(self,serializer):
                       serializer.save(user=self.request.user) 
            def get_queryset(self):
                    return Task.objects.filter(user=self.request.user)

class Register(generics.CreateAPIView,generics.GenericAPIView):
             serializer_class = UserSerializer
             queryset= User.objects.all()



