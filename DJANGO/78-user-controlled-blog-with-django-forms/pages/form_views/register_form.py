from django import forms
from pages.models import register_model


class RegisterForm(forms.ModelForm):
    class Meta:
        model = register_model
        fields = ("__all__")

        widgets = {
            "password" : forms.PasswordInput ( attrs = { "placeholders" : "Şifrenizi girin!" } ),
            "confirm_password" : forms.PasswordInput ( attrs = { "placeholders" : "Şifrenizi tekrar girin!" } ),
        }

