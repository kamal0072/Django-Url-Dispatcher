from django import forms

class EmployeForm(forms.Form):
    ename=forms.CharField(min_length=5,max_length=15,strip=False,label='Employee Name')

    epass=forms.CharField(widget=forms.PasswordInput(),label='Passwod',
    error_messages={'required':'Enter Your Correct Password'})

    email=forms.EmailField(required=True,label='Employee Email')

    def clean_name(self):
        data = self.cleaned_data["name"]
        if len(data)<4:
            raise forms.ValidationError('Enter More than Or Equal 4 char')
        return data

        data = self.cleaned_data["epass"]
        if len(data)<4:
            raise forms.ValidationError('Enter More than Or Equal 4 char')
        return data


  