from django.shortcuts import render
from django.http import HttpResponse
from .models import NewsArticlesList, Article

# Create your views here.

def index(response, id):
    ls = NewsArticlesList.objects.get(id=id)
    article = ls.article_set.get(id=1)
    return HttpResponse("<h1>%s<h1><br></br><p>%s</p>" %(ls.name, str(article.text)))

def home(response):
    pass