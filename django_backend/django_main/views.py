from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Article
from .forms import Submit_Form
import cloudinary
from cloudinary.models import CloudinaryField
from cloudinary.forms import CloudinaryFileField
from django.conf import settings
from rest_framework.generics import CreateAPIView
from rest_framework.parsers import MultiPartParser

# views.py, v1.5, May 29th 2023, Hugh Ding


def article_page(response, id):
    '''
    this function passes article objects to the article.html as parameters to be filled in

    Parameters:
        response: HttpRequest object that contains metadata about the request

    Returns:
        Render: Combines article.html with articles and returns an HttpResponse object with that rendered text.

    '''
    article = Article.objects.get(id=id)
    rec_articles = Article.objects.filter(approved=True).order_by('date')

    # Increase the view count by 1
    article.views += 1
    article.save()


    return render(response, 'main/article.html', {'article': article, 'recommended_articles': rec_articles[:3]}) # open dictionary

def home_trending(response):

    '''
    this function passes article objects to the home.html as parameters to be filled in

    Parameters:
        response: HttpRequest object that contains metadata about the request

    Returns:
        Render: Combines home.html with articles and returns an HttpResponse object with that rendered text.

    '''

    article_list = Article.objects.all().filter(approved=True).order_by('views')
    article1 = article_list[0]
    article_list2 = article_list[1::2]
    article_list3 = article_list[2::2]
    return render(response, 'main/home.html', {'article1': article1,'article_list2': article_list2, 'article_list3': article_list3 })

def home_opinion(response):
    '''
    this function passes article objects to the home.html as parameters to be filled in

    Parameters:
        response: HttpRequest object that contains metadata about the request

    Returns:
        Render: Combines home.html with articles and returns an HttpResponse object with that rendered text.

    '''
    article_list = Article.objects.filter(approved=True, opinion=False).order_by('date')
    article1 = article_list[0]
    article_list2 = article_list[1::2]
    article_list3 = article_list[2::2]
    return render(response, 'main/home.html', {'article1': article1,'article_list2': article_list2, 'article_list3': article_list3 })


def home_recent(response):

    '''
    this function passes article objects to the home.html as parameters to be filled in

    Parameters:
        response: HttpRequest object that contains metadata about the request

    Returns:
        Render: Combines home.html with articles and returns an HttpResponse object with that rendered text.

    '''
    
    article_list = Article.objects.all().filter(approved=True).order_by('date')
    article1 = article_list[0]
    article_list2 = article_list[1::2]
    article_list3 = article_list[2::2]
    return render(response, 'main/home.html', {'article1': article1, 'article_list2': article_list2, 'article_list3': article_list3 })


def submit_form(response):

    '''

    This function processes the information submitted from the html form to submit articles from students, creates a new Article object and saves to database

    Parameters:
        response: HttpRequest object that contains metadata about the request

    Return:
        Render: Combines a form.html with the form and returns an HttpResponse object with that rendered text.
    '''
    form = Submit_Form(response.POST, response.FILES)
    print(settings.CLOUDINARY)
    print(settings.CLOUDINARY_STORAGE)
    print(settings.CLOUDINARY['cloud_name'])
    print(settings.CLOUDINARY['api_key'])
    print(settings.CLOUDINARY['api_secret'])
    print(print(cloudinary.config().cloud_name))
    print(cloudinary.config().api_key)
    print(cloudinary.config().api_secret)

    if response.method == 'POST' and form.is_valid():
        print(settings.CLOUDINARY)
        print(settings.CLOUDINARY_STORAGE)
        author = form.cleaned_data['AuthorFirstName'] + ' ' + form.cleaned_data['AuthorLastName']
        title = form.cleaned_data['Title']
        subtitle = form.cleaned_data['Subtitle']
        text = form.cleaned_data['Text']
        text = text.split("//n")
        email = form.cleaned_data['Email']
        tags = form.cleaned_data['Tags']
        opinion = form.cleaned_data['Opinion']

        profile_pic_url = form.cleaned_data['ProfilePicture'].url
        # if profile_pic:
        #     storage = RawMediaCloudinaryStorage()
        #     uploaded_file = storage.save(author +'_profilepic', profile_pic)
        #     profile_pic_url = uploaded_file.url

        img = form.cleaned_data['TitlePicture'].url
        # if title_img:
        #     storage = RawMediaCloudinaryStorage()
        #     uploaded_file = storage.save(title + '_photo', title_img)
        #     title_img_url = uploaded_file.url

        # creates new article object with the information submitted by the form
        t = Article(author=author, title=title, subtitle=subtitle, text=text, email=email, tags=tags, opinion=opinion, profile_pic_url=profile_pic_url, img=img)
        # saves article in the database
        t.save()
        # redirects the user to thanks page
        return HttpResponseRedirect("/thanks")
    
    return render(response, "main/form.html", {"form":form})
    
    
def getTrueTags(tags, article):
    '''
    counts the number of tags an article has that match the tags given

    Parameters:
        tags: list of string of tags
    Returns:
        score: int, number of matches
    '''
    score = 0
    for tag in tags: 
        if tag in article.tags: score +=1
    return score

def search(response):

    '''
    gets information from the search bar which is a form, and eliminates and sorts articles based on search

    Parameters:
        response: HttpRequest object that contains metadata about the request

    return:
        Render: Combines home.html with articles and returns an HttpResponse object with that rendered text.
    '''

    # determines what the method of the response is
    if response.method =='POST':

        # get the answers from form
        t = response.POST.get("search_text")
        tags = []
        # appends to tags list if true
        if response.POST.get("Religion"): tags.append("Relgion")
        if response.POST.get("Politics"): tags.append("Politics")
        if response.POST.get("Events"): tags.append("Events")
        if response.POST.get("Environment"): tags.append("Environment")
        if response.POST.get("Business"): tags.append("Business")
        if response.POST.get("Sports"): tags.append("Sports")
        if response.POST.get("Events"): tags.append("Events")
        if response.POST.get("School"): tags.append("School")

        # creating a article list and sorting by date
        article_list = list(Article.objects.all().filter(approved=True).order_by('date'))
        article_list2 = []
        for article in article_list:
            if t in article.title or t in article.subtitle:
                article_list2.append(article)

        for index in range(len(article_list2)-1):
            key = getTrueTags(tags, article_list2[index])
            placeholder = index-1
            while placeholder >= 0 and getTrueTags(tags, article_list2[placeholder]) > key:
                article_list2[placeholder+1] = article_list2[placeholder]
                placeholder -= 1
            article_list2[placeholder+1] = article_list2[index]
    
    return render(response, "main/search.html", {"article_list":article_list})




def thanks(response):
    '''
    displays thanks.html

    returns:
        Render: Combines thanks.html with articles and returns an HttpResponse object with that rendered text.
    '''

    return render(response, 'main/thanks.html', {})

# to do:
# readme File
# fix search bug and the sorting bug (and make priority of words then tags) for home pages
# fix the admin save function