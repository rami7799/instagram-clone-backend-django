from django.contrib.auth import models
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post
from .forms import PostForm


class PostView(ListView, LoginRequiredMixin):
    model = Post
    template_name = "list.html"


class CreatePostView(CreateView):
    template_name = "new.html"
    model = Post
    form_class = PostForm
    context_object_name = 'form'

    def get_context_data(self, **kwargs):
        """Add User and profile to context."""
        context = super().get_context_data(**kwargs)
        context['profile'] = self.request.user.profile
        return context



