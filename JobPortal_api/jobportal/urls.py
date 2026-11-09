
from django.urls import path,include
from jobportal import views
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path('register/',views.Register.as_view()),
    path('login/',obtain_auth_token),
    path('jobs/',views.JObListandCreate.as_view()),
    path('jobs/<int:id>/',views.RetrieveUpdateDeleteJob.as_view())
]
