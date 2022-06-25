from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from .models import Post

# Create your views here.


class PostListView(ListView):
    # specify the model for list view
    model = Post


class PostCreateView(CreateView):
    model = Post

    fields = '__all__'

    success_url = ('blog: all')


class PostUpdateView(UpdateView):
    model = Post

    fields = '__all__'

    success_url = ('blog: all')


class PostDetailView(DetailView):
    model = Post


class PostDeleteView(DeleteView):
    model = Post

    fields = '__all__'

    success_url = ('blog: all')
