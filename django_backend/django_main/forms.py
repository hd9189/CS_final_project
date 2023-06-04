from django import forms
from cloudinary.forms import CloudinaryFileField
# forms.py, v1.3, May 29th 2023, Hugh Ding
# All the question djanog models fields for the submission form. 

TAGS = (('Sports', 'Sports'),
              ('Politics', 'Politics'),
              ('Business', 'Business'),
              ('Technology', 'Technology'),
              ('Environment', 'Environment'),
              ('Relgion', 'Religion'),
              ('Events', 'Events'),
              ('School', 'School')
              )


# This function comes from https://www.youtube.com/watch?v=sm1mokevMWk&t=9662s - this function initializes the django fields
# for the article submit form. The form has takes in inputs from the user and uploads them to the database by passing the information to views.py

# Inherits from the django forms module
class Submit_Form(forms.Form):

    '''
    This class is the questions/textboxes that the users will have to fill out to submit an article

    AuthorFirstName: Character Field (text input), First name of user
    AuthorLasttName: Character Field (text input), Last name of user
    Email: Email Field (input a email, meaning there must be a @...), email of user
    Title: Character Field, Title of article
    Subtitle: Character Field, subtitle of article    
    Tags: Multichoice field (boxes), tags/genres of article submitted
    Opinion: bool field, determinng whether the article is based on opinon or not
    ProiflePicture: Cloudinary field, uploads the profile picture image to imagecloud database. 
    TitlePicture: Title field, uploads the profile picture image to imagecloud database. 
 

    '''

    AuthorFirstName = forms.CharField(
        # what appears on the html form
        label="First Name",
        # it is required, however it explcitly states taht it needs to be filled in which doesn't look good, so it is done through widget
        required=False,
        max_length=200,
        widget= forms.TextInput(
            attrs={
                'class': 'author-f-name',
                'name': 'AuthorFName',
                'placeholder':'Enter First Name',
                'required': 'True'
                }
            )
        )
    AuthorLastName = forms.CharField(
        label="Last Name",
        required=False,
        max_length=200,
        widget= forms.TextInput(
            attrs={
                'class': 'author-l-name',
                'name': 'AuthorLName',
                'placeholder':'Enter Last Name',
                'required': 'True'
                }
            )
        )
    Email = forms.EmailField(
        max_length=300,
        required=False,
        widget= forms.EmailInput(
            attrs={
                'class': 'email',
                'name': 'email',
                'placeholder':'Enter Email',
                'required': 'True'
                }
            )
        )
    Title = forms.CharField(
        label="Title",
        max_length=200,
        required=False,
        widget= forms.TextInput(
            attrs={
                'class': 'title',
                'name': 'title',
                'placeholder':'Enter Title',
                'required': 'True'
                }
            )
        )
    
    Subtitle = forms.CharField(
        label="Subtitle",
        max_length=9999,
        required=False,
        widget= forms.TextInput(
            attrs={
                'class': 'sub-title',
                'name': 'sub-title',
                'placeholder':'Enter Sub Title',
                'required': 'True'
                }
            )
        )
    Text = forms.CharField(
        label="Text (use '//n' to indicate new paragraph)",
        required=False,
        max_length=99999999999999999999999999,
        widget=forms.Textarea(attrs={
            'class': 'article-text',
            'name': 'articleText',
            'placeholder':'Enter Article Text, use //n to indicate new paragraph',
            'required': 'True',
            'rows':8})
        )
    Tags = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=TAGS,
        )
    Opinion = forms.BooleanField(
        label='Opinion',
        required=False
        )
    ProfilePicture = CloudinaryFileField(
        label = 'Profile Picture',
        required=False
    )
    TitlePicture = CloudinaryFileField(
        label = 'Title Picture',
        required=False,
    )