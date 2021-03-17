from django import forms

class EmployeForm(forms.Form):
    e_name=forms.CharField(label='Employe Name:')
    e_email=forms.EmailField(label='Employe Email:')
    e_pass=forms.CharField(label='Employe Password')

