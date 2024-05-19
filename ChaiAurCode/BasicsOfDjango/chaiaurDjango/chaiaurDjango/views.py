from django.http import HttpResponse
from django.shortcuts import render

def Home(request):
    return render(request, 'website/index.html')

def About(request):
    return render(request, 'about.html')

def Contact(request):
    return render(request, 'contact.html')
