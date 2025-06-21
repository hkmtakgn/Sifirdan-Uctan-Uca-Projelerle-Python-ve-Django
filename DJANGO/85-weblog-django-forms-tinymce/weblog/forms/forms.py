from weblog.models import Blog_Post
from django import forms

from tinymce.widgets import TinyMCE


class PostForm(forms.ModelForm):
  content = forms.CharField(widget=TinyMCE(attrs={
      "cols": 80,
      "rows": 10,
      "style": "width:850px"
  }))

  class Meta:
    model = Blog_Post
    fields = "__all__"

    # widgets = {"content": forms.Textarea(attrs={"cols": 80, "rows": 10})}
