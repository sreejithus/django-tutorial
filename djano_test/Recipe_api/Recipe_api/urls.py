"""
URL configuration for Recipe_api project.

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

from Recipes import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('recipelist',views.Recipe_list.as_view()),
    path('recipecreate',views.Recipe_create.as_view()),
    path('retrieverecipe/<int:id>',views.Recipe_retrive.as_view()),
    path('fullupdaterecipe/<int:id>',views.Recipe_full_update.as_view()),
    path('partialupdaterecipe/<int:id>',views.Recipe_partial_update.as_view()),
    path('recipedelete/<int:id>',views.Recipe_delete.as_view())
]
