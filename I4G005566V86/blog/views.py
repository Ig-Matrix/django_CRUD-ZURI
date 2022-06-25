from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .models import Post

# Create your views here.
class PostListView(generic.ListView):
    model = Post

class PostCreateView(generic.CreateView):
    model = Post
    fields = '__all__'
    success_url  = reverse_lazy('blog:all')

class PostDetailView(generic.DetailView):
    model = Post

class PostUpdateView(generic.UpdateView):
    model = Post
    fields = '__all__'
    success_url  = reverse_lazy('blog:all')

class PostDeleteView(generic.DeleteView):
    model = Post
    fields = '__all__'
    success_url  = reverse_lazy('blog:all')