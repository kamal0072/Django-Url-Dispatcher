from django import forms

class EmployeForm(forms.Form):
    ename=forms.CharField(min_length=5,max_length=15,strip=False,
    label='Employee Name')

    epass=forms.CharField(widget=forms.PasswordInput(),label='Passwod',
    error_messages={'required':'Enter Your Correct Password'})

    email=forms.EmailField(required=True,label='Employee Email')

    def clean(self):
        cleaned_data=super().clean()
        e_name=self.cleaned_data['ename']
        e_pass=self.cleaned_data['epass']
        if len(e_name)<4:
            raise forms.ValidationError('Name Should Be more than 4')
        
        if len(e_pass)<4:
            raise forms.ValidationError('Enter More Than 4 Char')
        
