from django import forms
from django.core import validators
from .models import Student

#buil-in Validators

class EmployeForm(forms.ModelForm):
    ename=forms.CharField(initial='sonam',max_length=90,
    help_text='Enter Name Here')
    class Meta:
        model=Student
        fields=['id','ename','epass','email']
        labels={'ename':'Employee Name','epass':'Employee Password','email':'Employee Email'}
        help_text={'ename':'Enter Your Name Here..'}
        error_messages={
        'ename':{'required':'Name Mandatory'},
        'epass':{'required':'Enter Corrct Password'},
        'email':{'required':'Enter Correct Email'}
        }
        widgets={'epass':forms.PasswordInput(),
        'name':forms.TextInput(attrs={'ename':'cls','placeholder':'Mension your Name'})}


