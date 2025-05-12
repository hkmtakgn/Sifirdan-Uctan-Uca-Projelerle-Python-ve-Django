from pages.models import login_model
from django import forms


class LoginForm (forms.ModelForm):
    class Meta:
        model = login_model
        fields = ("username", "password")
        
    password = forms.CharField(widget=forms.PasswordInput)

