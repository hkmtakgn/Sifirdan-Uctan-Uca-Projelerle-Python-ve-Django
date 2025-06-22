from django import forms
from django.db.models import fields
from weblog.models import Blog_Post


class PostForm(forms.ModelForm):

  class Meta:
    model = Blog_Post
    fields = "__all__"
