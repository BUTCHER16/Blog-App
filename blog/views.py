from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
# Create your views here.

def home(request):
    content = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', content)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = '-date_posted'

class PostDetailView(DetailView):
    model = Post


def about(request):
    return render(request,'blog/about.html', {'title':'About'})