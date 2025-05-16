from django import forms
from my_stories.models import post_model


class PostForm(forms.ModelForm):

  class Meta:
    model = post_model
    fields = "__all__"
