from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Article
from .forms import Submit_Form
import cloudinary

from django.db.models import Q

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
    rec_articles = Article.objects.filter(approved=True).order_by('-date')

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

    article_list = Article.objects.all().filter(approved=True).order_by('-views')
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
    article_list = Article.objects.filter(approved=True, opinion=False).order_by('-date')
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
    
    article_list = Article.objects.all().filter(approved=True).order_by('-date')
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
    print(print(cloudinary.config().cloud_name))
    print(cloudinary.config().api_key)
    print(cloudinary.config().api_secret)

    if response.method == 'POST' and form.is_valid():
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
    Counts the number of tags an article has that match the tags given

    Parameters:
        tags: list of strings representing tags
        article: Article object

    Returns:
        score: int, number of matches
    '''
    score = 0
    for tag in tags:
        if tag in article.tags:
            score += 1
    return score

def search(response):
    '''
    Gets information from the search bar, eliminates, and sorts articles based on the search.

    Parameters:
        response: HttpRequest object that contains metadata about the request

    Returns:
        HttpResponse object with the rendered text
    '''
    if response.method == 'POST':
        # Get the input text from the form
        t = response.POST.get("search_text")

        tags = []
        # Append to tags list if true
        if response.POST.get("Religion"):
            tags.append("Religion")
        if response.POST.get("Politics"):
            tags.append("Politics")
        if response.POST.get("Events"):
            tags.append("Events")
        if response.POST.get("Environment"):
            tags.append("Environment")
        if response.POST.get("Business"):
            tags.append("Business")
        if response.POST.get("Sports"):
            tags.append("Sports")
        if response.POST.get("School"):
            tags.append("School")

        # Filter articles based on title or subtitle containing the input text
        article_list = list(Article.objects.filter(approved=True).filter(
            Q(title__contains=t) | Q(subtitle__contains=t)).order_by('-date'))

        # Sort articles using insertion sort based on the number of matching tags
        for i in range(1, len(article_list)):
            key = getTrueTags(tags, article_list[i])
            j = i - 1
            while j >= 0 and getTrueTags(tags, article_list[j]) < key:
                article_list[j + 1] = article_list[j]
                j -= 1
            article_list[j + 1] = article_list[i]

        return render(response, "main/search.html", {"article_list": article_list})



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