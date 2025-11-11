from weblog.models import Page, Interface_user, Post
from django import forms


class PageForm(forms.ModelForm):

  class Meta:
    fields = '__all__'
    model = Page


class UserForm(forms.ModelForm):

  class Meta:
    fields = "__all__"
    model = Interface_user

    exclude = ["is_online"]

    widgets = {
        "password": forms.TextInput(attrs={"type": "password"}),
        "re_password": forms.TextInput(attrs={"type": "password"})
    }


class PostForm(forms.ModelForm):

  class Meta:
    fields = "__all__"
    model = Post
