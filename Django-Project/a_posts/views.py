from django.shortcuts import render, redirect
from .models import Post
from django.forms import ModelForm
from django import forms
# Create your views here.
def home_view(request):
    posts = Post.objects.all()
    return render(request,'a_posts/home.html', {'posts':posts})



class PostCreateForm(ModelForm):
    class Meta:
        model = Post
        fields ='__all__'
        labels = {
            'body':'Caption',
        }
        widgets = {
            'body': forms.Textarea(attrs={'cols':80, 'rows':3, 'placeholder': 'Add a caption', 'class':'font1 text-4xl'}),
        }
    
def post_create_view(request):
    form = PostCreateForm()
    if request.method == 'POST':
        form = PostCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'a_posts/post_create.html', {'form':form})