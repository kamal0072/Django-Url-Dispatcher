from django import forms

class EmployeForm(forms.Form):
    e_name=forms.CharField(label='Employe Name:',label_suffix='-',
    help_text='Enter Emplyoye Name',initial="david")
    e_pass=forms.CharField(widget=forms.PasswordInput)
    e_email=forms.EmailField()
    