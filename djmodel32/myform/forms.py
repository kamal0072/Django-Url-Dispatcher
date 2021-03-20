from django import forms

class EmployeForm(forms.Form):
    e_name=forms.CharField(label='Employe Name:',label_suffix='-',
    help_text='Enter Emplyoye Name',initial="david")

    e_email=forms.EmailField(label='Employe Email:',initial='abc@gmail.com',
    help_text='Enter Employe Email',widget=forms.HiddenInput())

    # e_address=forms.CharField(initial='Enter Full Address',widget=forms.CheckboxInput(),
    # e_address=forms.CharField(initial='Enter Full Address',widget=forms.RadioSelect(),
    e_address=forms.CharField(initial='Enter Full Address',
    widget=forms.Textarea(),
    help_text='Enter Your Full Address')

    e_pass=forms.CharField(label='Employe Password',required=True,
    help_text='Enter maximum 70 char..',widget=forms.PasswordInput())
    e_phone=forms.CharField(widget=forms.HiddenInput())

