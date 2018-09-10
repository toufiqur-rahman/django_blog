from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'myBlog/post_list.html', {'posts': posts})
    Post.objects.get(pk=pk)


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'myBlog/post_detail.html', {'post': post})