from django.urls import path
from django.http import HttpResponse
from django.shortcuts import render

def Home(request):
    return HttpResponse("I am learnind djagno")
def About(request):
    return HttpResponse("Welcome to about section")
def Contact(request):
    return render(request,'contact.html')
urlpatterns = [
    path('', Home),
    path('about', About),
    path('contact', Contact),
]
