from django.shortcuts import render, get_object_or_404
from .models import Post
from django.http import Http404

# Create your views here.
def post_list(request):
    posts = Post.published.all()
    return render(request, 'blog/post/list.html', {'posts': posts})

def post_detail(request):
    posts = get_object_or_404(Post,id = id, status = Post.Status.PUBLISHED)
    
    return render(request, 'blog/post/details.html', {'posts': posts})
