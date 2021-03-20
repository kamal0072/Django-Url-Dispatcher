from django import forms

class EmployeForm(forms.Form):
    e_name=forms.CharField(label='Employe Name:',label_suffix='-',
    help_text='Enter Emplyoye Name',initial="david")

    e_email=forms.EmailField(label='Employe Email:',initial='abc@gmail.com',
    help_text='Enter Employe Email',widget=forms.HiddenInput())
    e_address=forms.CharField(initial='Enter Full Address',
    widget=forms.Textarea(),help_text='Enter Your Full Address')

    e_pass=forms.CharField(label="Enter a Valid Password",help_text="kamal@123",
    initial='abc@54321')
    