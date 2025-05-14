from django import forms
from pages.models import blog_post

class PostForm (forms.ModelForm):
    class Meta:
        model = blog_post
        fields = "__all__"
        