from django import forms
from weblog.models import Post
from tinymce.widgets import TinyMCE
from django.core import validators


def max_len_300(value):
  if len(value) > 300:
    raise forms.ValidationError("300 karakter uzunluğunu aştınız!")


class PostForm(forms.ModelForm):
  title = forms.CharField(validators=[
      validators.MaxLengthValidator(
          100, "Lütfen 100 karakterden kısa bir başlık girin!")
  ])

  content = forms.CharField(validators=[
      max_len_300,
  ],
                            widget=TinyMCE(
                                attrs={"placeholder": "Bir metin girin!"},
                                mce_attrs={"height": 200}))

  class Meta:
    model = Post
    fields = "__all__"

    # widgets = {
    #     "content":
    #     TinyMCE(attrs={
    #         "placeholder": "Metin girin!",
    #     },
    #             mce_attrs={"height": 200}),
    # }

  def clean_title(self):
    title = self.cleaned_data.get("title")
    if len(title) < 3:
      raise forms.ValidationError("En az 3 karakter giriniz!")
    return title
