from django.contrib.auth.views import LoginView
from django.urls import path
from .views import *


urlpatterns = [
    path('signup' , SignUp.as_view()),
    path('login' , LoginView.as_view())
]