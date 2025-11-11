from blog.models import add_story_model
from django import forms


class PostForm (forms.ModelForm) :
    class Meta:
        model = add_story_model
        fields = ("username","avatar","post_content","dept")

        