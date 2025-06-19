from django import forms
from weblog.models import Blog
from tinymce.widgets import TinyMCE


class BlogForm(forms.ModelForm):
  content = forms.CharField(widget=TinyMCE(attrs={"cols": 77, "rows": 33}))

  class Meta:
    model = Blog
    fields = [
        "username",
        "department",
        "language",
        "content",
    ]

    # widgets = {
    #     "content": forms.Textarea(attrs={"placeholder": "Enter a text!"})
    # }


# content alanı için iki farklı yerde widget tanımlanmaz !
# Ya Meta içinde widgets yada doğrudan content = forms.Charfield (....) gibi
