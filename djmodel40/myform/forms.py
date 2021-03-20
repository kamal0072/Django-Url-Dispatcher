from django import forms

class EmployeForm(forms.Form):
    ename=forms.CharField(min_length=5,max_length=15,strip=False,label='Employee Name')

    epass=forms.CharField(widget=forms.PasswordInput(),label='Employee Password',
    error_messages={'required':'Enter Your Correct Password'})

    eemail=forms.EmailField(required=True,label='Employee Email')
    
    fname=forms.BooleanField(label='Father Name')
    
    roll=forms.IntegerField(error_messages={'required':'Enter a valid Roll Number'},
    min_value=2,max_value=5,label='Employee Roll Number')
    
    agree=forms.DecimalField(min_value=2,max_digits=12)