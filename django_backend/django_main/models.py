from django.db import models

#terminal comands
# python manage.py makemigrations
# python manage.py migrate
# python manage.py shell
    # [variable] = NewsArticlesList(name='...)
    # [variable].save()
    # [variable].article_set.create([parameter stuff])
    # t = NewsArticlesList.object: get all the objects
        # t.filter(name_startswith="MHS"): filters through all the objects and find the ones that starts with that

# python mange.py createsuperuser: this is to create an admin account
    # Username: hugh
    # email: hding1@ocdsb.ca
    # pw: 1234


# Create your models here.
# create a database class for all the stuff
class NewsArticlesList(models.Model):
    # CharField is a field where we can store information, basically a string
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
 
class Article(models.Model):
    # ForeignKey for objects
    # This links to the NewsArticlesList, and makes it automatically have a list/set of Article objects in it 
    newsarticleslist = models.ForeignKey(NewsArticlesList, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    views = models.BigIntegerField()
    likes = models.BigIntegerField()
    Author = models.CharField(max_length=100)
    Date = models.DateField()
    # Img = models.ImageField(upload_to=filepath)
    
    def __str__(self):
        return self.text

    
