from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Post

class BlogAdminForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={'id': "richtext_field"}))


    class Meta:
        model = Post
        fields = '__all__'
