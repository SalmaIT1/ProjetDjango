from django.shortcuts import render, redirect , get_object_or_404
from .models import *
from .forms import *

def Post(request):
    posts = PostModel.objects.all()
    return render(request, 'blog/post.html', {'posts': posts})


def post_detail(request, post_id):
    post = PostModel.objects.get(id=post_id)
    context = {
        'post': post,
        'image_url': post.image.url if post.image else None,
    }
    return render(request, 'blog/post_detail.html', context)
    



