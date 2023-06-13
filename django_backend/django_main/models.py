from django.db import models
from datetime import date
from multiselectfield import MultiSelectField
from cloudinary.models import CloudinaryField

# models.py, v1.12, May 27th 2023, Hugh Ding


#terminal comands
# python manage.py makemigrations
# python manage.py migrate
# python manage.py shell
    # [variable] = Article(name='...)
    # [variable].save()
    # [variable].article_set.create([parameter stuff])
    # t = NewsArticlesList.object: get all the objects
        # t.filter(name_startswith="MHS"): filters through all the objects and find the ones that starts with that

# python manage.py createsuperuser: this is to create an admin account
    # Username: hugh
    # email: hding1@ocdsb.ca
    # pw: 1234


# Create your models here.
# create a database class for all the stuff
 

from django.db import models
from django.utils import timezone
from cloudinary.models import CloudinaryField

# Source: https://www.youtube.com/watch?v=sm1mokevMWk&t=9662s
# This class is to store all essential information regarding each article. For every article, one of the Article objefts are created and store in there
# Establishes django fields for Article class. 
# inherits from django models module
# This function comes from https://www.youtube.com/watch?v=sm1mokevMWk&t=9662s - this function initializes the django fields and helps create the model
class Article(models.Model):

    '''
    Article object that represent an individual article that will be displayed on the pages and viewed by the users

    TAGS: list, 2d list of tuples with the tag choices for the users
    title: character field/str, title of article
    subtitle: character field, subtitle of article
    text: JSON field (list), text/content of article
    views: BigInteger field/int, the number of views of the object
    date: date field, date of submission of article
    tags: Multiselect field/list, generes or tags attached to article
    opinion: bool field, whether or not the article is an opinion article
    email: email field/str, email of author
    profile_pic_url: cloudinary field/str, a url of an profile picture image from the cloudinary API
    img: cloudinary field/str, a url of an title image from the cloudinary API
    REQUIRED_FIELDS: list, list of strings of the required fields to be known

    '''


    TAGS = [('Sports', 'Sports'),
              ('Politics', 'Politics'),
              ('Business', 'Business'),
              ('Technology', 'Technology'),
              ('Environment', 'Environment'),
              ('Relgion', 'Religion'),
              ('Events', 'Events'),
              ('School', 'School')
              ]


    # ForeignKey for objects
    # This links to the NewsArticlesList, and makes it automatically have a list/set of Article objects in it 
    title = models.CharField(max_length=200, default=False)
    subtitle = models.CharField(max_length=9999, default=False)
    text = models.JSONField()
    views = models.BigIntegerField(default=0)
    author = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    tags = MultiSelectField(choices=TAGS, max_choices=3, max_length=20, default=None)
    opinion = models.BooleanField(default=True)
    email = models.EmailField(default='example@email.com')
    profile_pic_url = CloudinaryField('profile_pic', default=False)
    img = CloudinaryField('title_img', default=False)
    approved = models.BooleanField(default=False)
    REQUIRED_FIELDS = ['title', 'text', 'author','email', 'date','approved', 'tags', 'opinion']
    
    # def __str__(self):
    #     return self.text
