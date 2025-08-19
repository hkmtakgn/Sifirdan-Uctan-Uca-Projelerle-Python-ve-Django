from django import forms
from weblog.models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = "__all__"
        widgets = {
            "content":
            forms.Textarea(attrs={
                "placeholder": "Metin giriniz!",
                "style": "height:177px"
            }),
        }
