from django.shortcuts import render
from django.http import HttpResponse
from .models import Article

# Create your views here.

def index(response, id):
    return render(response, 'main/base.html', {}) # open dictionary

def home(response):
    return render(response, 'main/home.html', {})