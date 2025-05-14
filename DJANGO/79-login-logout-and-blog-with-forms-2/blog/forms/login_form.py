from blog.models import login_model
from django import forms

class LoginForm (forms.ModelForm):
    class Meta:
        model = login_model
        fields = ("username", "password")

        widgets = {
            "username":forms.TextInput(attrs={"placeholders": "Lütfen kullanıcı adınızı giriniz!",}),
            "password":forms.PasswordInput(attrs={"placeholders": "Lütfen şifrenizi giriniz!",}),
        }

