from django.contrib import admin 
from django.contrib.auth.admin import UserAdmin
from .models import Article
# Register your models here.

class ArticleAdmin(UserAdmin):
    ordering = ['title', 'date']# order of display
    list_display = ('title', 'date', 'tags', 'text', 'views', 'likes', 'opinion') # whatever you want to display on admin
    search_fields = () # what you can search for
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

# Can see list db on site
admin.site.register(Article, ArticleAdmin)
