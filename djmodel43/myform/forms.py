from django import forms
from django.core import validators

#buil-in Validators

class EmployeForm(forms.Form):
    ename=forms.CharField(validators=[validators.MaxLengthValidator(5)])

    epass=forms.CharField(validators=[validators.MaxLengthValidator(10)],
    label="Password")

    email=forms.EmailField(validators=[validators.MaxLengthValidator(20)])
