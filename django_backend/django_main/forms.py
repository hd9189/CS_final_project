from django import forms
from cloudinary.forms import CloudinaryFileField


TAGS = (('Sports', 'Sports'),
              ('Politics', 'Politics'),
              ('Business', 'Business'),
              ('Technology', 'Technology'),
              ('Environment', 'Environment'),
              ('Relgion', 'Religion'),
              ('Events', 'Events')
              )

class Submit_Form(forms.Form):
    AuthorFirstName = forms.CharField(
        label="First Name",
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
        label='Text',
        required=False,
        max_length=99999999999999999999999999,
        widget=forms.Textarea(attrs={
            'class': 'article-text',
            'name': 'articleText',
            'placeholder':'Enter Article Text',
            'required': 'True',
            'rows':8})
        )
    Tags = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=TAGS,
        )
    Opinion = forms.BooleanField(
        label='Opnion',
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