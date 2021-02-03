from django.shortcuts import render
from django.views import generic

from .models import Post
# Create your views here.



class HomePageView(generic.ListView):
    model = Post
    template_name = 'blog/index.html'

class BlogDetailView(generic.DetailView):
    model  = Post
    template_name = 'blog/pos_detail.html'


class BlogCreateView(generic.CreateView):
    template_name = 'blog/post_new.html'
    model = Post
    fields = ['title', 'author', 'body']