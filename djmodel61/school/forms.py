from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class UserCreationForm(UserCreationForm):
    password1=forms.CharField(label='New Password:',widget=forms.PasswordInput())
    password2=forms.CharField(label='Confirm Password:',widget=forms.PasswordInput())
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
        labels={'username':'USER NAME:','first_name':'FIRST NAME:',
        'last_name':'LAST NAME:','email':'EMAIL ADDRESS:'}