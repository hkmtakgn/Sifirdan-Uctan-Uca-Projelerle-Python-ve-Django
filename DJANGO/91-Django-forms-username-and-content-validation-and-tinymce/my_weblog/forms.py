from django import forms
from my_weblog.models import PostModel
from tinymce.widgets import TinyMCE
from django.core import validators


#1.Yöntem ↓
def min_len_3(value):
    if len(value) < 3:
        raise forms.ValidationError("En az 3 karakter uzunluğunda olmalı!")


#----------------------------


class PostForm(forms.ModelForm):
    #TinyMCE 2.Yöntem ↓
    # content = forms.CharField(widget=TinyMCE(
    #     attrs={"placeholder": "Bir metin girin!"}))
    #------------------------
    #1.Yöntem ↓
    username = forms.CharField(validators=[
        min_len_3,
    ])
    #------------------------
    #2.Yöntem ↓
    content = forms.CharField(
        validators=[
            validators.MaxLengthValidator(300, "300 karakteri aşamaz!")
        ],
        widget=TinyMCE(attrs={"placeholder": "Bir metin girin!"}))

    #------------------------

    class Meta:
        model = PostModel
        fields = [
            "username",
            "content",
            "is_active",
            "post_img",
        ]

        # exclude = [
        #     "is_active",
        # ]

        widgets = {
            "username":
            forms.TextInput(attrs={"placeholder": "Enter your username !"}),
            #TinyMCE 1.Yöntem ↓
            "content":
            TinyMCE(attrs={"placeholder": "Lütfen bir metin girin!"}),
            #-----------------
        }
