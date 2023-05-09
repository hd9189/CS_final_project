from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
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

def article_page(response, id):
    article = Article.objects.get(id=id)
    rec_articles = Article.objects.filter('-approved').order_by('date')

    # Increase the view count by 1
    article.views += 1
    article.save()


    return render(response, 'main/article.html', {'article': article, 'recommended_articles': rec_articles}) # open dictionary

def home_trending(response):
    article_list = Article.objects.all().filter(approved=True).order_by('views')

    article_list2 = article_list[0::2]
    article_list3 = article_list[1::2]
    return render(response, 'main/home.html', {'article1': article_list[0],'article_list2': article_list2, 'article_list3': article_list3 })

def home_opinion(response):
    article_list = Article.objects.filter(approved=True, opinion=False).order_by('date')
    article_list2 = article_list[0::2]
    article_list3 = article_list[1::2]
    return render(response, 'main/home.html', {'article1': article_list[0],'article_list2': article_list2, 'article_list3': article_list3 })


def home_recent(response):
    article_list = Article.objects.all().filter(approved=True).order_by('date')
    article_list2 = article_list[0::2]
    article_list3 = article_list[1::2]
    return render(response, 'main/home.html', {'article1': article_list[0],'article_list2': article_list2, 'article_list3': article_list3 })


def submit_form(response):
    form = Submit_Form(response.POST, response.FILES)

    if response.method == 'POST' and form.is_valid():
        author = form.cleaned_data['AuthorFirstName'] + ' ' + form.cleaned_data['AuthorLastName']
        title = form.cleaned_data['Title']
        subtitle = form.cleaned_data['Subtitle']
        text = form.cleaned_data['Text']
        email = form.cleaned_data['Email']
        tags = form.cleaned_data['Tags']
        opinion = form.cleaned_data['Opinion']
        profile_pic = form.cleaned_data['ProfilePicture']
        title_img = form.cleaned_data['TitlePicture']


        t = Article(author=author, title=title, subtitle=subtitle, text=text, email=email, tags=tags, opinion=opinion)
        t.save()
        return HttpResponseRedirect("/thanks")
    
    return render(response, "main/form.html", {"form":form})
    

def thanks(response):
    return render(response, 'main/thanks.html', {})