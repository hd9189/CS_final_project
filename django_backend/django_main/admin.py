from django.contrib import admin 
from django.contrib.auth.admin import UserAdmin
from .models import Article
# Register your models here.

# admin.py, v1.1, April 13th 2023, Hugh Ding

# This function helps manage the Article part of the administration, which the client will interact with. 
class ArticleAdmin(UserAdmin):
    # order of display
    ordering = ['title', 'date']
    # what should be displayed on the admin page
    list_display = ('title', 'subtitle', 'date', 'tags', 'text', 'views', 'opinion', 'img','approved') # whatever you want to display on admin
    # what you can search for
    search_fields = () 
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    # Allows the apporoved attribute of the object to be edited by the admin
    list_editable=['approved']

# Can see list db on site
admin.site.register(Article, ArticleAdmin)
