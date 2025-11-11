from django import forms
from django.core import validators
from my_weblog.models import PostModel

#2. Yöntem ↓
# from django.core import validators

# 3.Yöntem ↓
from django.core import validators


#3.Yöntem ↓
def min_length_3(value):
    if len(value) < 3:
        raise forms.ValidationError("Lütfen 3 karakterden fazla giriniz!")


class PostForm(forms.ModelForm):
    #2.Yöntem ↓
    # username = forms.CharField(validators=[
    #     validators.MinLengthValidator(3, "Lütfen en az 3 karakter giriniz!")
    # ])

    #3.Yöntem ↓
    username = forms.CharField(validators=[
        min_length_3,
    ])

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
            "content":
            forms.Textarea(attrs={"placeholder": "Write something !"})
        }

    # 1.Yöntem ↓
    # def clean_username(self):
    #     username = self.cleaned_data.get("username")
    #     if len(username) < 3:
    #         raise forms.ValidationError('Lütfen en az 3 karakter giriniz!')
    #     return username
