from django.contrib.auth import views
from .models import Profile
from django.views.generic.edit import CreateView, DeleteView, UpdateView



class SignUp(CreateView):
    template_name = "user/signup.html"
    model = Profile
    fields = ['website', 'biography', 'phone_number', 'picture', ]
    success_message = "New student successfully added."


class Loginview(views.LoginView):
    template_name = "user/login.html"
    redirect_authenticated_user = True

    def form_valid(self , form):
        form.save()
        return super().form_valid(form)

