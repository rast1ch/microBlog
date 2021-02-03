from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

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


class BlogUpdateView(generic.UpdateView):
    template_name = 'blog/post_edit.html'
    model = Post
    fields = ['title', 'body']


class BlogDeleteView(generic.DeleteView):
    template_name = 'blog/post_delete.html'
    model = Post
    success_url = reverse_lazy('blog:index')
