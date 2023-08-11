from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from .models import Post
# Create your views here.
class HomePageView(ListView):
    model = Post
    template_name = 'home.html'

class PostDetailPageView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class NewPostPageView(CreateView):
    model = Post
    template_name = 'new_post.html'
    fields = ['title','author','body']
class EditPostPageView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title','body']

class DeletePostPageView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')
