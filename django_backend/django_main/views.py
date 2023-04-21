from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
from .forms import Submit_Form

from rest_framework.generics import CreateAPIView
from rest_framework.parsers import MultiPartParser

from .models import Image
from .serializers import ImageSerializer


class UploadImage(CreateAPIView):

    serializer_class = ImageSerializer
    parser_classes = (MultiPartParser,)
    queryset = Image.objects.all()


# Create your views here.

def index(response, id):
    return render(response, 'main/base.html', {}) # open dictionary

def home(response):
    return render(response, 'main/home.html', {})

def submit_form(response):
    form = Submit_Form(response.POST)

    if form.is_valid():
        author = form.cleaned_data['AuthorFirstName'] + ' ' + form.cleaned_data['AuthorLastName']
        title = form.cleaned_data['Title']
        text = form.cleaned_data['Text']
        email = form.cleaned_data['Email']
        tags = form.cleaned_data['Tags']
        opinion = form.cleaned_data['Opinion']

        t = Article(author=author, title=title, text=text, email=email, tags=tags, opinion=opinion)
        t.save()
    return render(response, "main/form.html", {"form":form})

def thanks(response):
    return render(response, 'main/thanks.html', {})