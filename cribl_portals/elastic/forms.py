from django import forms
from .models import ElasticDestination

class AddClusterForm(forms.ModelForm):
    title = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Title", "class": "form-control"}), label="")
    description = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Description", "class": "form-control"}), label="")
    username = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Username", "class": "form-control"}), label="")
    password = forms.CharField(required=True, widget=forms.widgets.PasswordInput(attrs={"placeholder": "Password", "class": "form-control"}), label="")
    url = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "URL", "class": "form-control"}), label="")

    class Meta:
        model = ElasticDestination
        exclude = ("message", "status")