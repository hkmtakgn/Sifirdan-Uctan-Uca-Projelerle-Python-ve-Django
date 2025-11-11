from django import forms
from my_weblog.models import PostModel


class PostForm(forms.ModelForm):

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

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if len(username) < 3:
            raise forms.ValidationError('Lütfen en az 3 karakter giriniz!')
        return username
