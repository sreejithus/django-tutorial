from django.contrib import admin
from django.urls import path
from events import views

urlpatterns = [
              path('event',views.CreateorList.as_view()),
              path('event/<int:id>',views.RetriveUpdateDelete.as_view())
]
