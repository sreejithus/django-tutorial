from Recipe.models import Recipe,Review
from rest_framework import serializers
from django.contrib.auth.models import User

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Recipe
        fields='__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','password','email','first_name','last_name']

    def create(self,validated_data):
        u=User.objects.create_user(**validated_data)
        u.save()
        return u

class ReviewSerializer(serializers.ModelSerializer):
    recipe =serializers.StringRelatedField()  #string related
    user= serializers.StringRelatedField()

    message = serializers.SerializerMethodField()#metho related
    user= serializers.SerializerMethodField()
    recipe = serializers.SerializerMethodField()

    user = UserSerializer(read_only=True)#nested serializer
    recipe = RecipeSerializer
    class Meta:
        model=Review
        fields='__all__'
        read_only_fields =['user',]
        def get_message(self,obj):
                  return 'hello'
        def get_user(self,obj):
                  return obj.user.username
        def get_recipe(self,obj):
                  return obj.recipe.recipe_name