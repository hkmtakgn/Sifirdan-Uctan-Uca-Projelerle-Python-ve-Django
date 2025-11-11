from django import forms
from django.forms import widgets
from security_control.models import Visitor, Subcontractor


class VisitorForm(forms.ModelForm):

  class Meta:
    model = Visitor
    fields = '__all__'


class SubcontractorForm(forms.ModelForm):

  class Meta:
    model = Subcontractor
    fields = '__all__'
