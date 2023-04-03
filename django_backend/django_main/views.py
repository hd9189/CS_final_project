from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
from .forms import Submit_Form

# Create your views here.

def index(response, id):
    return render(response, 'main/base.html', {}) # open dictionary

def home(response):
    return render(response, 'main/home.html', {})

def submit_form(response):
    form = Submit_Form()
    return render(response, "main/form.html", {"form":form})