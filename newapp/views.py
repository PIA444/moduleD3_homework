from django.views.generic import ListView, DetailView
from .models import Author, Category, Post, PostCategory, Comment

class PostsList(ListView):
    model = Post
    template_name = 'posts.html'
    context_object_name = 'posts'
    queryset = Post.objects.order_by('-id')

class PostList(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'


