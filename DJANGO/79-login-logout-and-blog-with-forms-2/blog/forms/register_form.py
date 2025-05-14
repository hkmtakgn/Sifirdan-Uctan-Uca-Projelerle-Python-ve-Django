from blog.models import register_model
from django import forms


class RegisterForm (forms.ModelForm):
    class Meta:
        model = register_model
        fields = "__all__"

        widgets = {
            "password":forms.PasswordInput (attrs={"placeholders":"Şifrenizi girin!"}),
            "confirm_password":forms.PasswordInput (attrs={"placeholders":"Şifrenizi tekrar girin!"}),
        }

    