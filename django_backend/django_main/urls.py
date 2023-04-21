# urls to go to the different views in views.py
from django.urls import path
from . import views # . refers to the django_main file


urlpatterns = [
    # go directly to the index page as default
    # makes index need an int parameter, makes the url need a /[id] to get to that page.
    # so the stirng in the front is for the unique id of the page, 
    path('<int:id>', views.index, name='index'),
    path("", views.home, name="home"),
    path("submit/", views.submit_form, name='submit'),
    path("thanks/", views.thanks, name='thanks'),
    path("image/upload", views.UploadImage.as_view())

] 
