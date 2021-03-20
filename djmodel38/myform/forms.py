from django import forms

class EmployeForm(forms.Form):
    ename=forms.CharField()
    epass=forms.CharField(widget=forms.PasswordInput())
    eemail=forms.EmailField()
    