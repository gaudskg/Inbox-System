from curses.ascii import HT
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request,'home.html')

def inbox(request):
    return render(request,'inbox.html')

def login(request):
    return render(request,'registration/login.html')