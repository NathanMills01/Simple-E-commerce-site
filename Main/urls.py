from unicodedata import name
from django.urls import path 
from . import views

urlpatterns = [

    path("home/", views.home, name = "home"),
    path("Items/", views.Items, name = "Items"), 
    path("Services/", views.Services, name = "Services")
]

#It seems the routes need to be the same as the functions