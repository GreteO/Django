from django.shortcuts import render
from django.views import generic
from .models import Post
from django.views.generic import ListView, CreateView 
from django.urls import reverse_lazy 

from .forms import PostForm

class PostList(generic.ListView):

    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'


class CreatePostView(generic.CreateView):
    model = Post
    form_class = PostForm
    template_name = 'newpost.html'
    success_url = reverse_lazy('home')
