from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class SignUp(UserCreationForm):
    password2=forms.CharField(label='Enter Password(Again)',
    widget=forms.PasswordInput())
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
        labels={'email':'email'}