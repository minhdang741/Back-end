from django.db import models
from django import forms


# Create your models here.

class LoginForm(forms.Form):
    email = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())

"""
    def clean_email(self):
        email = self.cleaned_data['email']

    def clean_password(self):
        password = self.cleaned_data['password']
"""
