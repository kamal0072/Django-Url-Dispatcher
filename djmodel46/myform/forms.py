from django import forms
from django.core import validators

#buil-in Validators

class EmployeForm(forms.Form):
    ename=forms.CharField(validators=[validators.MaxLengthValidator(5)],
    label='Employee Name')

    epass=forms.CharField(max_length=90,widget=forms.PasswordInput(),
    label='Enter Password')
    

    email=forms.EmailField(validators=[validators.MaxLengthValidator(20)],
    label='User Email')
