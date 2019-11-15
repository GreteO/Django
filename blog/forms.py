from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title','cover', 'content', 'author', 'slug', 'status']
        list_filter = ("status",)
        search_fields = ['title', 'content']