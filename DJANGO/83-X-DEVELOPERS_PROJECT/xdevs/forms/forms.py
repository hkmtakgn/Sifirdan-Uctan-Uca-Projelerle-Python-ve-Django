from autoslug import fields
from django import forms
from xdevs.models import Web_Pages


class Add_Page_Form(forms.ModelForm):

  class Meta:
    model = Web_Pages
    fields = "__all__"
