"""
URL configuration for expense_tracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from Spending import views

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
     path('admin/', admin.site.urls),
     path('register',views.Register_user.as_view()),
     path('login',obtain_auth_token),
     path('currentloggedin',views.Current_Loggedin.as_view()),
     path('expensecreate',views.ExpenseCreate.as_view()),
     path('expenselist',views.ExpenseList.as_view()),
      path('expenselist/<int:id>',views.ExpenseRetrive.as_view()),
      path('expensesummery',views.ExpenseSummery.as_view()),
      path('getbudgetplan',views.ExpenseBudgetPlan.as_view())
    
]
