from django.contrib import admin 
from django.contrib.auth.admin import UserAdmin
from .models import Article
# Register your models here.

class ArticleAdmin(UserAdmin):
    ordering = ['title', 'date']# order of display
    list_display = ('title', 'subtitle', 'date', 'tags', 'text', 'views', 'likes', 'opinion', 'approved') # whatever you want to display on admin
    search_fields = () # what you can search for
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    list_editable=['approved']

# Can see list db on site
admin.site.register(Article, ArticleAdmin)
