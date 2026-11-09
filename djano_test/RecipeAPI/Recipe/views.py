from django.db.models.query_utils import Q
from django.shortcuts import render,get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from Recipe.models import Recipe,Review
from rest_framework.response import Response
from Recipe.serializers import RecipeSerializer,UserSerializer
from rest_framework import status


# Create your views here.

class CreateRecipe(APIView):
    def post(self,request):
        form_data=request.data
        serializer_instance=RecipeSerializer(data=form_data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)

class RecipeList(APIView):
    def get(self,request):
        r=Recipe.objects.all()
        serializer_instance=RecipeSerializer(r,many=True)
        return Response(serializer_instance.data,status=status.HTTP_200_OK)

class RetrieveRecipe(APIView):
    def get(self,request,id):
        r=get_object_or_404(Recipe,id=id)
        serializer_instance=RecipeSerializer(r)
        return Response(serializer_instance.data,status=status.HTTP_200_OK)

class FullUpdateRecipe(APIView):
    def put(self,request,id):
        form_data=request.data
        r=get_object_or_404(Recipe,id=id)
        serializer_instance=RecipeSerializer(r,data=form_data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)

class PartialUpdateRecipe(APIView):
    def patch(self,request,id):
        form_data=request.data
        r=get_object_or_404(Recipe,id=id)
        serializer_instance=RecipeSerializer(r,data=form_data,partial=True)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)

class DeleteRecipe(APIView):
    def delete(self,request,id):
        r=get_object_or_404(Recipe,id=id)
        r.delete()
        return Response({'Message':'Recipe Data Deleted'},status=status.HTTP_204_NO_CONTENT)

class SearchRecipe(APIView):
    def get(self,request):
        data=self.request.query_params.get('search')
        r=Recipe.objects.filter(Q(title__icontains=data) | Q(ingredients__icontains=data))
        if not r.exists():
            return Response({'Message':'No Record Found'},status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer_instance=RecipeSerializer(r,many=True)
            return Response(serializer_instance.data,status=status.HTTP_200_OK)

class UserRegister(APIView):
    def post(self,request):
        form_data=request.data
        serializer_instance=UserSerializer(data=form_data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)

class UserLogout(APIView):
    def get(self,request):
        print(self.request.user)
        self.request.user.auth_token.delete()
        return Response({'Message': 'Logged Out Successfully'})


from .permissions import Isowner
from .serializers import ReviewSerializer
class CreateReview(APIView):
             permission_classes=[IsAuthenticated,Isowner]
            
             def post(self,request):
                        serializer_instance =  ReviewSerializer(data= request.data)

                        if serializer_instance.is_valid():
                                 serializer_instance.save(user=request.user)
                                 return Response(serializer_instance.data,status=status.HTTP_201_CREATED)

                        else:
                             return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)

class ReadReview(APIView):
            permission_classes=[IsAuthenticated,Isowner]
            def get(self,request,id):
                            data = Review.objects.filter(recipe=id)
                            serializer_instance =ReviewSerializer(data,many=True)
                            return Response(serializer_instance.data,status=status.HTTP_200_OK)

class UpdateReview(APIView):
               permission_classes=[IsAuthenticated,Isowner]
               def put(self,request,id):
                             r=get_object_or_404(Review,id=id)
                             self.check_object_permissions(request,r)
                           

                             serializer_instance = ReviewSerializer(r,data=request.data)
                             if serializer_instance.is_valid():
                                       serializer_instance.save()
                                       return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
                             else:
                                  return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)

               def  patch(self,request,id):
                                            d = get_object_or_404(Review,id=id)
                                            self.check_object_permissions(request,d)
                                            serializer_instance = ReviewSerializer(d,data=request.data,partial=True)
                                            if serializer_instance.is_valid():
                                                       serializer_instance.save()
                                                       return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
                                            else:
                                                  return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)

class Reviewdelete(APIView):
             permission_classes=[IsAuthenticated,Isowner]
             
             def delete(self,request,id):
                              d = get_object_or_404(Review,id=id)
                              self.check_object_permission(request,d)
                              d.delete()
                              return Response(status=status.HTTP_204_NO_CONTENT)