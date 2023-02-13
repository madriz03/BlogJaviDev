from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post, Comment

# Create your views here.

def index(request):
    post = Post.objects.all()
    context = {
        'post': post
    }
    return render(request, 'post/index.html', context)


def detail(request, id):
    post = Post.objects.get(id=id)
    comment = Comment.objects.filter(post=post)

    context = {
        'post': post,
        'comment': comment
    }
    return render(request, 'post/detail.html', context)


def add_comment(request, id):
    post = Post.objects.get(id=id)
    if request.method == 'POST':
        comment = Comment(text_comment=request.POST['comment'], post=post, author=request.user)
        comment.save()
   
    return redirect('detail', id=id)
    