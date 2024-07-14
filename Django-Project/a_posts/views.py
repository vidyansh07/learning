from django.shortcuts import render

# Create your views here.
def home_view(request):
    title = 'Welcome to my blog'
    return render(request,'index.html', {"title": title})
