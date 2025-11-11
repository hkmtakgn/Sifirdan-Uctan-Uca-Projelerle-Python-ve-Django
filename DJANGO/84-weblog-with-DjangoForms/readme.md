# settings.py
pip install django-tinymce
INSTALLED_APPS = [
    "tinymce",
]

# models.py ↓↓↓
from django.db import models
from tinymce import models as tinymce_model


class Blog(models.Model):
  username = models.CharField(max_length=100)
  department = models.CharField(max_length=100)
  language = models.CharField(max_length=100)
  # content = models.TextField(blank=True, null=True)
  content = tinymce_model.HTMLField(null=True, blank=True)


# forms.py ↓↓↓

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


# home.html ↓↓↓

{% extends 'core/base.html' %}

{% block content %}
{{ post_form }}
{{ post_form.media }}
{% include 'components/list-group.html' %}
{% endblock content %}

# admin.py ↓↓↓

from django.contrib import admin
from weblog.models import Blog

# Register your models here.


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
  list_display = [
      "username",
      "department",
      "language",
  ]


