# urls to go to the different views in views.py
from django.urls import path
from . import views # . refers to the django_main file
from django.conf import settings
from django.conf.urls.static import static


# forms.py, v1.3, June 1st 2023, Hugh Ding


urlpatterns = [
    # go directly to the index page as default
    # makes index need an int parameter, makes the url need a /[id] to get to that page.
    # so the stirng in the front is for the unique id of the page, 

    # home pages
    path("", views.home_recent, name='recent'),
    path('<int:id>/', views.article_page, name='article'),

    # builds the url paths and when this url is ran a certain function from views.py is run
    path("trending/", views.home_trending, name='trending'),
    path("trending/<int:id>", views.article_page, name='article'),

    path("opinion/", views.home_opinion, name='opinion'),
    path("opinion/<int:id>", views.article_page, name='article'),
    
    path("search/", views.search, name='search'),
    path("search/<int:id>", views.article_page, name='article'),

    
    path("submit_form/", views.submit_form, name='submit_form'),
    path("thanks/", views.thanks, name='thanks'),
] 
