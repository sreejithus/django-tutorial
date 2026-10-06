"""
URL configuration for demopro project.

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
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('goodmorning',views.Goodmorning.as_view(),name='goodmoring'),
    path('goodevening',views.Goodevening.as_view(),name='goodevening'),
    path('helloworld',views.Helloworld.as_view(),name='helloworld'),
    path('userdetails',views.Userdetails.as_view(),name='userdetails'),
    path('student',views.Studentlist.as_view()),
    path('addstudent',views.Addstudent.as_view()),
    path('studentdetail/<int:i>',views.StudentDetail.as_view()),
    path('studentdelete/<int:i>',views.StudentDelete.as_view()),
     path('studentupdate/<int:i>',views.StudentFullUpdate.as_view()),
      path('studentpartialupdate/<int:i>',views.StudentPartialUpdate.as_view()),

]
