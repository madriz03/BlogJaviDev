from django.shortcuts import render, redirect
from .models import Post, Comment
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

def index(request):
    post = Post.objects.all().order_by('-date')
    context = {
        'post': post
    }
    return render(request, 'post/index.html', context)




def detail(request, id, slug):
    post = Post.objects.get(id=id, slug=slug)
    comment = Comment.objects.filter(post=post)

    context = {
        'post': post,
        'comment': comment
    }

    return render(request, 'post/detail.html', context)




@login_required
def add_comment(request, id, slug):
    post = Post.objects.get(id=id)
    if request.method == 'POST':
        comment_text = request.POST.get('comment', '').strip()
        if comment_text:
            comment = Comment(text_comment=request.POST['comment'], post=post, author=request.user)
            comment.save()
            messages.success(request, "Se agrego tu comentario")
       
            
    return redirect('detail', id=id, slug=slug)




def comment_delete(request, id, slug):
    comment = Comment.objects.get(id=id)
    if request.user == comment.author:
        comment.delete()
        messages.success(request, "Eliminaste tu comentario")
        return redirect('detail', id=comment.post.id, slug=comment.post.slug)
    
    else:
        # Agregar Message de error
        return redirect('detail', id=comment.post.id, slug=comment.post.slug)
    