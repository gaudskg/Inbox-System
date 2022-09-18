import importlib
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required #login required to access private pages
from django.views.decorators.cache import cache_control #Destroy the session after logout
# Create your views here.

def home(request):
    return render(request,'home.html')

@login_required(login_url='login')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def inbox(request):
    return render(request,'inbox.html')

# def login(request):
#     return render(request,'registration/login.html')