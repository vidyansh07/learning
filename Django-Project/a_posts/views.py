from django.shortcuts import render, redirect
from .models import Post
from django.forms import ModelForm
from django import forms
from bs4 import BeautifulSoup
import requests
# Create your views here.
def home_view(request):
    posts = Post.objects.all()
    return render(request,'a_posts/home.html', {'posts':posts})



class PostCreateForm(ModelForm):
    class Meta:
        model = Post
        fields =['url','body']
        labels = {
            'body':'Caption',
        }
        widgets = {
            'body': forms.Textarea(attrs={'cols':80, 'rows':3, 'placeholder': 'Add a caption', 'class':'font1 text-4xl'}),
            'url': forms.FileInput(attrs={'placeholder':'Add the url'})
        }
    
def post_create_view(request):
    form = PostCreateForm()
    if request.method == 'POST':
        form = PostCreateForm(request.POST, request.FILES)
        if form.is_valid():
            post =form.save(commit=False)
            
            website = requests.get(form.data['url'])           
            sourcecode = BeautifulSoup(website.text, 'html.parser')
            
            find_image = sourcecode.select('meta[content^="https://live.staticflickr.com/"]')
            image = find_image[0].get('content')
            post.image = image
            
            find_title = sourcecode.select('h1.photo-title')
            title = find_title[0].text.strip()
            post.title = title
            
            find_artist = sourcecode.select('a.owner-name')
            artist = find_artist[0].text.strip()
            post.artist = artist           
            
            post.save()
            return redirect('home')
    return render(request, 'a_posts/post_create.html', {'form':form})