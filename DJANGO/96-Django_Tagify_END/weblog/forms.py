from django import forms
from django.core import validators
# from django.db import models
from weblog.models import Post
from tinymce.widgets import TinyMCE
from django.utils.html import strip_tags
from django.core.exceptions import ValidationError


# 2.Yontem ↓
def max_length_99(value):
  if len(value) > 99:
    raise forms.ValidationError("99 karakteri asamaz!")


class PostForm(forms.ModelForm):
  # form valıdatıon 2 yontem ↓ :
  title = forms.CharField(validators=[
      max_length_99,  # ← 2.Yontem
      validators.MinLengthValidator(
          3, "Lutfen en az 3 karakter girin!")  # ← 1.Yontem
  ])

  content = forms.CharField(widget=TinyMCE(
      attrs={"placeholder": "Metin girin!"}))

  class Meta:
    fields = "__all__"
    model = Post

    exclude = ["tag"]

  # widgets = {"content": forms.Textarea(attrs={"style": "height:33vh;"})}
  # widgets = {"content": TinyMCE(attrs={"cols": 80, "rows": 30}, )}

  # Form Validation 1.Yontem ↓ :
  # def clean_title(self):
  #   title = self.cleaned_data.get("title")
  #   if len(title) < 3:
  #     raise forms.ValidationError("Lutfen en az 3 karakter girin!")
  #   return title

  # content alanı ıcın tınymce ıle valıdatıon kullanımı ↓ :
  def clean_content(self):
    content = self.cleaned_data.get("content", "")

    # HTML etiketlerini kaldır (TinyMCE içerikleri genellikle <p> gibi HTML içerir)
    text = strip_tags(content).strip()

    if len(text) < 3:
      raise ValidationError("Lütfen en az 3 karakter girin!")

    return content
