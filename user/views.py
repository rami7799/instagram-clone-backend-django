import django
from django.shortcuts import render
from django.views.generic import CreateView
from .models import Profile

class SignUp(CreateView):
    template_name = "user/signup.html"
    model = Profile
    fields = "__all__"
    success_message = "New student successfully added."

