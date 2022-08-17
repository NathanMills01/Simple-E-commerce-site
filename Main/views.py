from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(response):
    return render(response, "Main/Home.html")

def Services(response):
    return render(response, "Main/Services.html")

def Items(response):
    return render(response, "Main/Items.html")
