from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm
from django.http import HttpResponse


# Create your views here.

def Welcome(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
    else:
        form = RegisterForm()
        
    return render(response, "index.html", {"form":form})

