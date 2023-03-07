from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *

# Create your views here.
class News(ListView):
    model = Post
    template_name = 'news/news.html'
    context_object_name = 'news'
    queryset = Post.objects.order_by('-publish_time')

class Post(DetailView):
    model = Post
    template_name = 'news/post.html'
    context_object_name = 'post'

