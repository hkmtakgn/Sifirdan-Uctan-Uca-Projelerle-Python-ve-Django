from blog.models import post_model
from django import forms


class PostForm(forms.ModelForm):

  class Meta:
    model = post_model
    fields = "__all__"

    widgets = {
        "content": forms.Textarea(attrs={"placeholder": "Birşeyler yaz!"}),
    }
