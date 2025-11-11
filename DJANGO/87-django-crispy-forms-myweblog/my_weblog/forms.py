from django import forms
from my_weblog.models import PostModel


class PostForm(forms.ModelForm):

    class Meta:
        model = PostModel
        fields = "__all__"

        # exclude = [
        #     "is_active",
        # ]

        widgets = {
            "username":
            forms.TextInput(attrs={"placeholder": "Enter your username !"}),
            "content":
            forms.Textarea(attrs={"placeholder": "Write something !"})
        }
