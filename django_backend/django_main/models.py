from django.db import models
from datetime import date
from multiselectfield import MultiSelectField
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


class Image(models.Model):

    image = CloudinaryField("image")
    timestamp = models.DateTimeField(default=timezone.now)

    @property
    def image_url(self):
        return (
            f"https://res.cloudinary.com/ddmhkhmvz/{self.image}"
        )


class Article(models.Model):

    TAGS = (('Sports', 'Sports'),
              ('Politics', 'Politics'),
              ('Business', 'Business'),
              ('Technology', 'Technology'),
              ('Environment', 'Environment'),
              ('Relgion', 'Religion'),
              ('Events', 'Events')
              )


    # ForeignKey for objects
    # This links to the NewsArticlesList, and makes it automatically have a list/set of Article objects in it 
    title = models.CharField(max_length=200, default=False)
    text = models.CharField(max_length=300)
    views = models.BigIntegerField(default=0)
    likes = models.BigIntegerField(default=0)
    author = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    tags = MultiSelectField(choices=TAGS, max_choices=3, max_length=20, default=None)
    opinion = models.BooleanField(default=True)
    email = models.EmailField(default='example@email.com')
    # profile_pic = models.ImageField()
    approved = models.BooleanField(default=False)
    REQUIRED_FIELDS = ['title', 'text', 'author','email', 'date','approved', 'tags', 'opinion']
    
    def __str__(self):
        return self.text

    
