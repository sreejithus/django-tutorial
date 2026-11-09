"""
URL configuration for RecipeAPI project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Recipe import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('createrecipe',views.CreateRecipe.as_view()),
    path('recipelist',views.RecipeList.as_view()),
    path('retriverecipe/<int:id>',views.RetrieveRecipe.as_view()),
    path('fullupdaterecipe/<int:id>',views.FullUpdateRecipe.as_view()),
    path('partialupdaterecipe/<int:id>',views.PartialUpdateRecipe.as_view()),
    path('deleterecipe/<int:id>',views.DeleteRecipe.as_view()),
    path('searchrecipe',views.SearchRecipe.as_view()),
    path('userregister',views.UserRegister.as_view()),
    path('userlogin',obtain_auth_token),
    path('userlogout',views.UserLogout.as_view()),
    path('createreview',views.CreateReview.as_view()),
    path('reviews/<int:id>',views.ReadReview.as_view()),
    path('updatereview/<int:id>',views.UpdateReview.as_view()),
    path('deletereview/<int:id>',views.Reviewdelete.as_view()),
]
