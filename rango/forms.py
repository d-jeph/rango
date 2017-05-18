from django import forms
from django.contrib.auth.models import User
from rango.models import Category,Page

class CategoryForm(forms.ModelForm):
    name= forms.CharField(max_length=128,help_text="Category name")
    views = forms.IntegerField(widget=forms.HiddenInput(),initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(),initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(),required=False)

    class Meta:
        model = Category
        fields= ('name',)
class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=128,help_text='Page Title')
    url = forms.URLField(max_length=200,help_text='Page Url')
    views = forms.IntegerField(widget=forms.HiddenInput(),initial=0)

    class Meta:
        model = Page
        fields = ('title', 'url', 'views')
        # or say exclude = ('category',)

    def clean(self): #to clean a url
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')

        # If url is not empty and doesn't start with 'http://',then prepend 'http://'.
        if url and not url.startswith('http://'):
            url = 'http://' + url
            cleaned_data['url'] = url
            return cleaned_data
