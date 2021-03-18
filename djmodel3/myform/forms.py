from django import forms

class EmployeForm(forms.Form):
    e_name=forms.CharField(label='Employe Name:',label_suffix='-',help_text='Enter Emplyoye Name',initial="david")
    e_email=forms.EmailField(label='Employe Email:',initial='abc@gmail.com',help_text='Enter Employe Email')
    e_pass=forms.CharField(label='Employe Password',required=True,initial='Raj@123',
    help_text='Enter maximum 70 char..')
    # key=forms.CharField(widget=forms.HiddenInput())
    

