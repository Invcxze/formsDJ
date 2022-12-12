from django import forms

class UserForm(forms.Form):
    name = forms.CharField()
    surname = forms.CharField()
    country = forms.CharField()
    city = forms.CharField()
    street = forms.CharField()
    home = forms.IntegerField()
    