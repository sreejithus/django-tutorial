from django.contrib import admin
from django.urls import path
from booking import views

urlpatterns = [
              path('booking',views.CreateorList.as_view()),
              path('booking/<int:id>',views.RetriveUpdateDelete.as_view()),
              path("booking_cancell/<int:id>",views.Cancell_view.as_view())
]