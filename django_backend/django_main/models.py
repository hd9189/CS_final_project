from django.db import models
from taggit.managers import TaggableManager
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
 
class Article(models.Model):
    # ForeignKey for objects
    # This links to the NewsArticlesList, and makes it automatically have a list/set of Article objects in it 
    title = models.CharField(max_length=200, default=False)
    text = models.CharField(max_length=300)
    views = models.BigIntegerField(default=0)
    likes = models.BigIntegerField(default=0)
    author = models.CharField(max_length=100)
    date = models.DateField()
    tags = TaggableManager()
    opinion = models.BooleanField()
    profile_pic = models.ImageField(upload_to='profile_pic/%Y/%m/%d/', max_length=255, null=True)
    REQUIRED_FIELDS = ['title', 'text', 'author', 'date', 'tags']
    
    def __str__(self):
        return self.text

    
