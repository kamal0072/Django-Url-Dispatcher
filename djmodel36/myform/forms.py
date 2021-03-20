from django import forms

class EmployeForm(forms.Form):
    e_name=forms.CharField(label='Employe Name:',label_suffix='-',
    help_text='Enter Emplyoye Name',initial="david")

    e_email=forms.EmailField()

    e_pass=forms.CharField(widget=forms.PasswordInput)
    e_pass1=forms.CharField(widget=forms.HiddenInput)
    e_pass2=forms.CharField(widget=forms.Textarea)
    e_pass3=forms.CharField(widget=forms.TextInput())
    e_pass4=forms.CharField(widget=forms.FileInput())
    e_pass5=forms.CharField(widget=forms.TextInput(attrs={'attr':'css1'}))
    