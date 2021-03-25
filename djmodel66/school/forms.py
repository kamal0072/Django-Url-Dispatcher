from django.contrib.auth.forms import UserCreationForm,UserChangeForm,SetPasswordForm
from django.contrib.auth.models import User
from django import forms


class SignUp(UserCreationForm):
    password2=forms.CharField(label='Enter Password(Again)',
    widget=forms.PasswordInput())
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
        labels={'email':'email'}

class EditUserForm(UserChangeForm):
    password=None
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','date_joined','last_login']
        labels={'email':'Email'}

class EditAdminForm(UserChangeForm):
    password=None
    
    class Meta:
        model=User
        fields='__all__'
        labels={'email':'Email'}

class SetpawdFrom(SetPasswordForm):
    password=None
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','date_joined','last_login']
        labels={'email':'Email'}