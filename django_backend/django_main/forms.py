from django import forms

class Submit_Form(forms.Form):
    AuthorFirstName = forms.CharField(label="First Name", max_length=200)
    AuthorLastName = forms.CharField(label="Last Name", max_length=200)
    Email = forms.EmailField(max_length=300)
    Title = forms.CharField(label="Title", max_length=200)
    Text = forms.CharField(label='Text', max_length=100000000000)
    # ProfilePicture = forms.ImageField(upload_to='profile_pic/%Y/%m/%d/', max_length=255, null=True)