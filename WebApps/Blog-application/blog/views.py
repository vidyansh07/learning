from django.shortcuts import render, get_object_or_404
from .models import Post    
# from .models import Job
from django.http import Http404


# Create your views here.
def post_list(request):
    posts = Post.published.all
    return render(request, 'blog/post/list.html', {'posts': posts})

def post_detail(request,id):
    post = get_object_or_404(Post, id = id, status=Post.Status.PUBLISHED)
    return render(request, 'blog/post/details.html', {'post': post})
# def job_list(request):
#     jobs = Job.published.all()
#     return render(request, 'blog/job/list.html', {'job': jobs})

# def job_detail(request, slug):
#     job = get_object_or_404(Job, slug=slug, status=Job.Status.PUBLISHED)
#     return render(request, 'blog/job/detail.html', {'job': job})
