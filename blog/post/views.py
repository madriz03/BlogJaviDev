from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.

def index(request):
    post = Post.objects.all()
    context = {
        'post': post
    }
    return render(request, 'post/index.html', context)


def detail(request, id):
    post = Post.objects.get(id=id)
    context = {
        'post': post
    }
    return render(request, 'post/detail.html', context)